# 2017.02.03 21:50:42 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_view.py
from gui import SystemMessages
from gui.Scaleform.daapi import LobbySubView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_parameters import IVehCompareView, VehCompareBasketParamsCache
from gui.Scaleform.daapi.view.meta.VehicleCompareViewMeta import VehicleCompareViewMeta
from gui.Scaleform.framework import g_entitiesFactories
from gui.Scaleform.framework.entities.DAAPIDataProvider import ListDAAPIDataProvider
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE
from gui.game_control.veh_comparison_basket import MAX_VEHICLES_TO_COMPARE_COUNT
from gui.shared import g_itemsCache
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import selectVehicleInHangar, showVehiclePreview
from gui.shared.formatters import text_styles
from gui.shared.items_parameters.formatters import getAllParametersTitles
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.game_control import IVehicleComparisonBasket
from tutorial.loader import g_loader
_BACK_BTN_LABELS = {VIEW_ALIAS.LOBBY_HANGAR: 'hangar',
 VIEW_ALIAS.LOBBY_STORE: 'shop',
 VIEW_ALIAS.LOBBY_RESEARCH: 'researchTree',
 VIEW_ALIAS.LOBBY_TECHTREE: 'researchTree'}

class VehicleCompareView(LobbySubView, VehicleCompareViewMeta):
    __background_alpha__ = 0.0
    comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)

    def __init__(self, ctx = None):
        super(VehicleCompareView, self).__init__(ctx)
        self.__vehDP = None
        self.__paramsCache = None
        self.__backAlias = ctx.get('previewAlias', VIEW_ALIAS.LOBBY_HANGAR)
        return

    def closeView(self):
        self.onBackClick()

    def onSelectModulesClick(self, vehicleID, index):
        g_loader.stopOnceOnlyHint('VehCompareConfig')
        event = g_entitiesFactories.makeLoadEvent(VIEW_ALIAS.VEHICLE_COMPARE_MAIN_CONFIGURATOR, ctx={'index': int(index)})
        self.fireEvent(event, scope=EVENT_BUS_SCOPE.LOBBY)

    def onRemoveAllVehicles(self):
        self.comparisonBasket.removeAllVehicles()

    def onRemoveVehicle(self, index):
        self.comparisonBasket.removeVehicleByIdx(int(index))

    def onRevertVehicle(self, index):
        self.comparisonBasket.revertVehicleByIdx(int(index))

    def onGoToPreviewClick(self, vehicleID):
        intVehicleID = int(vehicleID)
        vehicle = g_itemsCache.items.getItemByCD(intVehicleID)
        if vehicle.isPreviewAllowed():
            showVehiclePreview(intVehicleID, VIEW_ALIAS.VEHICLE_COMPARE)
        else:
            SystemMessages.pushI18nMessage(SYSTEM_MESSAGES.VEHICLECOMPARE_PREVIEWNOTALLOWED, vehicle=vehicle.userName, type=SystemMessages.SM_TYPE.Error)

    def onGoToHangarClick(self, vehicleID):
        selectVehicleInHangar(int(vehicleID))

    def onParamDeltaRequested(self, index, paramID):
        deltas = self.__paramsCache.getParametersDelta(int(index), paramID)
        self.as_setParamsDeltaS({'paramID': paramID,
         'deltas': deltas})
        self.__updateDifferenceAttention()

    def onBackClick(self):
        event = g_entitiesFactories.makeLoadEvent(self.__backAlias)
        self.fireEvent(event, scope=EVENT_BUS_SCOPE.LOBBY)

    def _populate(self):
        super(VehicleCompareView, self)._populate()
        self.as_setStaticDataS({'header': self.__getHeaderData()})
        self.as_setVehicleParamsDataS(getAllParametersTitles())
        self.__vehDP = VehiclesDataProvider()
        self.__vehDP.setFlashObject(self.as_getVehiclesDPS())
        self.__paramsCache = VehCompareBasketParamsCache(self.__vehDP)
        self.__updateUI()
        self.comparisonBasket.onChange += self.__updateUI
        self.comparisonBasket.onSwitchChange += self.__onVehCmpBasketStateChanged
        self.comparisonBasket.onParametersChange += self.__onVehicleParamsChanged

    def _dispose(self):
        super(VehicleCompareView, self)._dispose()
        self.comparisonBasket.onChange -= self.__updateUI
        self.comparisonBasket.onSwitchChange -= self.__onVehCmpBasketStateChanged
        self.comparisonBasket.onParametersChange -= self.__onVehicleParamsChanged
        self.__paramsCache.dispose()
        self.__paramsCache = None
        self.__vehDP.fini()
        self.__vehDP = None
        self.comparisonBasket.writeCache()
        return

    def __updateUI(self, *data):
        self.as_setVehiclesCountTextS(text_styles.main(_ms(VEH_COMPARE.VEHICLECOMPAREVIEW_TOPPANEL_VEHICLESCOUNT, count=text_styles.stats(self.comparisonBasket.getVehiclesCount()))))
        self.__updateDifferenceAttention()

    def __onVehCmpBasketStateChanged(self):
        """
        gui.game_control.VehComparisonBasket.onSwitchChange event handler
        """
        if not self.comparisonBasket.isEnabled():
            self.destroy()

    def __getHeaderData(self):
        key = _BACK_BTN_LABELS.get(self.__backAlias, 'hangar')
        backBtnDescrLabel = '#veh_compare:header/backBtn/descrLabel/{}'.format(key)
        return {'closeBtnLabel': VEH_COMPARE.HEADER_CLOSEBTN_LABEL,
         'backBtnLabel': VEH_COMPARE.HEADER_BACKBTN_LABEL,
         'backBtnDescrLabel': backBtnDescrLabel,
         'titleText': text_styles.promoSubTitle(VEH_COMPARE.VEHICLECOMPAREVIEW_HEADER)}

    def __updateDifferenceAttention(self):
        """
        Show/hide difference attention icon(WOTD-68988).
        Two or more different tanks have difference crew or modules -> show icon, otherwise - hide
        """
        vehiclesCount = self.comparisonBasket.getVehiclesCount()
        if vehiclesCount > 1 and len(set(self.comparisonBasket.getVehiclesCDs())) > 1:
            comparisonDataIter = self.comparisonBasket.getVehiclesPropertiesIter(lambda vehCmpData: (vehCmpData.getConfigurationType(), vehCmpData.getCrewData()))
            prevModuleType, prevCrewData = next(comparisonDataIter)
            for moduleType, crewData in comparisonDataIter:
                if prevModuleType != moduleType or prevCrewData != crewData:
                    break
                prevModuleType, prevCrewData = moduleType, crewData

    def __onVehicleParamsChanged(self, _):
        self.__updateDifferenceAttention()


class VehiclesDataProvider(ListDAAPIDataProvider, IVehCompareView):

    def __init__(self):
        super(VehiclesDataProvider, self).__init__()
        self.__list = []

    @property
    def sortedCollection(self):
        return self.collection

    @property
    def collection(self):
        return self.__list

    def emptyItem(self):
        return None

    def buildList(self, *args):
        self.__list = args[0] if args else []
        if len(self.__list) < MAX_VEHICLES_TO_COMPARE_COUNT:
            self.__list.append({'isFirstEmptySlot': True})
        self.refresh()

    def updateItems(self, *args):
        data = args[0]
        self.refreshRandomItems(range(0, len(data)), data)

    def clear(self):
        self.__list = []

    def fini(self):
        self.clear()
        self._dispose()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\vehicle_compare\cmp_view.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:42 St�edn� Evropa (b�n� �as)
