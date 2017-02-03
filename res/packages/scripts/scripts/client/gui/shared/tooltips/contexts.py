# 2017.02.03 21:52:42 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/tooltips/contexts.py
import constants
import gui
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK
from CurrentVehicle import g_currentVehicle, g_currentPreviewVehicle
from collections import namedtuple
from gui.Scaleform.daapi.view.lobby.server_events import events_helpers
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers
from gui.goodies.goodies_cache import g_goodiesCache
from gui.shared.items_parameters import params_helper
from gui.shared.items_parameters.formatters import NO_BONUS_SIMPLIFIED_SCHEME
from helpers import dependency
from shared_utils import findFirst
from gui.shared import g_itemsCache
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.Tankman import TankmanSkill
from gui.shared.gui_items.dossier import factories, loadDossier
from gui.shared.tooltips import TOOLTIP_COMPONENT
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.shared.fortifications.FortOrder import FortOrder
from gui.shared.formatters import text_styles
from helpers.i18n import makeString
from items import vehicles
from gui.Scaleform.genConsts.CUSTOMIZATION_ITEM_TYPE import CUSTOMIZATION_ITEM_TYPE
from skeletons.gui.server_events import IEventsCache

def _getCmpVehicle():
    return cmp_helpers.getCmpConfiguratorMainView().getCurrentVehicle()


def _getCmpInitialVehicle():
    return cmp_helpers.getCmpConfiguratorMainView().getInitialVehicleData()


class StatsConfiguration(object):
    __slots__ = ('vehicle', 'sellPrice', 'buyPrice', 'unlockPrice', 'inventoryCount', 'vehiclesCount', 'node', 'xp', 'dailyXP', 'minRentPrice', 'restorePrice', 'rentals', 'slotIdx', 'futureRentals')

    def __init__(self):
        self.vehicle = None
        self.sellPrice = False
        self.buyPrice = True
        self.minRentPrice = True
        self.restorePrice = True
        self.rentals = True
        self.futureRentals = False
        self.unlockPrice = True
        self.inventoryCount = True
        self.vehiclesCount = True
        self.node = None
        self.xp = True
        self.dailyXP = True
        self.slotIdx = 0
        return


class StatusConfiguration(object):
    __slots__ = ('vehicle', 'slotIdx', 'eqs', 'checkBuying', 'node', 'isAwardWindow', 'isResearchPage', 'checkNotSuitable', 'showCustomStates')

    def __init__(self):
        self.vehicle = None
        self.slotIdx = 0
        self.eqs = tuple()
        self.checkBuying = False
        self.node = None
        self.isResearchPage = False
        self.isAwardWindow = False
        self.checkNotSuitable = False
        self.showCustomStates = False
        return


class ParamsConfiguration(object):
    __slots__ = ('vehicle', 'params', 'crew', 'eqs', 'devices', 'dossier', 'dossierType', 'isCurrentUserDossier', 'historicalBattleID', 'checkAchievementExistence', 'simplifiedOnly', 'externalCrewParam')

    def __init__(self):
        self.vehicle = None
        self.params = True
        self.crew = True
        self.eqs = True
        self.devices = True
        self.dossier = None
        self.dossierType = None
        self.isCurrentUserDossier = True
        self.historicalBattleID = -1
        self.simplifiedOnly = False
        self.externalCrewParam = False
        self.checkAchievementExistence = True
        return


class ToolTipContext(object):
    """ Root class for tool tip call context
    """

    def __init__(self, component, fieldsToExclude = None):
        self._component = component
        self._fieldsToExclude = fieldsToExclude or tuple()

    @property
    def fieldsToExclude(self):
        return self._fieldsToExclude

    def buildItem(self, *args, **kwargs):
        return None

    def getStatusConfiguration(self, item):
        return StatusConfiguration()

    def getStatsConfiguration(self, item):
        return StatsConfiguration()

    def getParamsConfiguration(self, item):
        return ParamsConfiguration()

    def getComponent(self):
        return self._component

    def getParams(self):
        """ Additional params that may be provided by context.
        """
        return {}


class ShopContext(ToolTipContext):

    def __init__(self, fieldsToExclude = None):
        super(ShopContext, self).__init__(TOOLTIP_COMPONENT.SHOP, fieldsToExclude)

    def buildItem(self, intCD):
        return g_itemsCache.items.getItemByCD(int(intCD))

    def getStatusConfiguration(self, item):
        value = super(ShopContext, self).getStatusConfiguration(item)
        value.checkBuying = True
        value.showCustomStates = True
        return value

    def getStatsConfiguration(self, item):
        value = super(ShopContext, self).getStatsConfiguration(item)
        value.xp = False
        value.dailyXP = False
        return value

    def getParamsConfiguration(self, item):
        value = super(ShopContext, self).getParamsConfiguration(item)
        value.params = gui.GUI_SETTINGS.technicalInfo
        value.eqs = False
        value.devices = False
        return value


class AwardContext(ShopContext):
    """ Context for award carousel's items.
    """

    def __init__(self, fieldsToExclude = None):
        super(AwardContext, self).__init__(fieldsToExclude)
        self._tmanRoleLevel = None
        self._rentExpiryTime = None
        return

    def buildItem(self, intCD, tmanCrewLevel = None, rentExpiryTime = None):
        self._tmanRoleLevel = tmanCrewLevel
        self._rentExpiryTime = rentExpiryTime
        return g_itemsCache.items.getItemByCD(int(intCD))

    def getStatsConfiguration(self, item):
        value = super(AwardContext, self).getStatsConfiguration(item)
        value.sellPrice = False
        value.buyPrice = False
        value.unlockPrice = False
        value.inventoryCount = False
        value.vehiclesCount = False
        value.futureRentals = True
        return value

    def getStatusConfiguration(self, item):
        value = super(AwardContext, self).getStatusConfiguration(item)
        value.isAwardWindow = True
        return value

    def getParamsConfiguration(self, item):
        value = super(AwardContext, self).getParamsConfiguration(item)
        value.simplifiedOnly = True
        value.externalCrewParam = True
        return value

    def getParams(self):
        return {'tmanRoleLevel': self._tmanRoleLevel,
         'rentExpiryTime': self._rentExpiryTime}


class InventoryContext(ToolTipContext):

    def __init__(self, fieldsToExclude = None):
        super(InventoryContext, self).__init__(TOOLTIP_COMPONENT.INVENTORY, fieldsToExclude)

    def buildItem(self, intCD):
        return g_itemsCache.items.getItemByCD(int(intCD))

    def getStatsConfiguration(self, item):
        value = super(InventoryContext, self).getStatsConfiguration(item)
        value.buyPrice = False
        value.minRentPrice = False
        value.unlockPrice = False
        value.sellPrice = True
        value.xp = getattr(item, 'xp', 0) > 0
        value.dailyXP = True
        return value

    def getParamsConfiguration(self, item):
        value = super(InventoryContext, self).getParamsConfiguration(item)
        value.params = gui.GUI_SETTINGS.technicalInfo
        return value


class CarouselContext(InventoryContext):

    def __init__(self, fieldsToExclude = None):
        super(InventoryContext, self).__init__(fieldsToExclude)
        self._component = TOOLTIP_COMPONENT.CAROUSEL

    def getStatusConfiguration(self, item):
        value = super(CarouselContext, self).getStatusConfiguration(item)
        value.checkNotSuitable = True
        return value

    def getStatsConfiguration(self, item):
        value = super(CarouselContext, self).getStatsConfiguration(item)
        value.rentals = True
        return value

    def buildItem(self, invID):
        return g_itemsCache.items.getVehicle(int(invID))


class PotapovQuestsChainContext(ToolTipContext):
    """ Private quests context of chain
    """

    def __init__(self, fieldsToExclude = None):
        super(PotapovQuestsChainContext, self).__init__(TOOLTIP_COMPONENT.HANGAR, fieldsToExclude)

    def buildItem(self, tileID, chainID):
        return (tileID, chainID)


class PotapovQuestsTileContext(ToolTipContext):
    """  Private quests context of tile
    """

    def __init__(self, fieldsToExclude = None):
        super(PotapovQuestsTileContext, self).__init__(TOOLTIP_COMPONENT.HANGAR, fieldsToExclude)

    def buildItem(self, tileID):
        return events_helpers.getPotapovQuestsCache().getTiles().get(tileID)


class QuestContext(ToolTipContext):
    """ Common quest class for tool tip context
    """
    eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, fieldsToExclude = None):
        super(QuestContext, self).__init__(TOOLTIP_COMPONENT.HANGAR, fieldsToExclude)

    def buildItem(self, eventID):
        return self.eventsCache.getEvents().get(eventID, None)


class BaseHangarParamContext(ToolTipContext):

    def __init__(self, showTitleValue = False):
        super(BaseHangarParamContext, self).__init__(TOOLTIP_COMPONENT.HANGAR)
        self.showTitleValue = showTitleValue

    def getComparator(self):
        return params_helper.idealCrewComparator(g_currentVehicle.item)

    def buildItem(self, *args, **kwargs):
        return g_currentVehicle.item


class HangarParamContext(BaseHangarParamContext):

    def __init__(self):
        super(HangarParamContext, self).__init__(True)
        self.formatters = NO_BONUS_SIMPLIFIED_SCHEME


class PreviewParamContext(HangarParamContext):

    def __init__(self):
        super(PreviewParamContext, self).__init__()
        self.formatters = NO_BONUS_SIMPLIFIED_SCHEME

    def getComparator(self):
        return params_helper.vehiclesComparator(g_currentPreviewVehicle.item, g_currentPreviewVehicle.defaultItem)

    def buildItem(self, *args, **kwargs):
        return g_currentPreviewVehicle.item


class CmpParamContext(HangarParamContext):

    def __init__(self):
        super(CmpParamContext, self).__init__()
        self.formatters = NO_BONUS_SIMPLIFIED_SCHEME

    def getComparator(self):
        return params_helper.vehiclesComparator(_getCmpVehicle(), _getCmpInitialVehicle()[0])


class HangarContext(ToolTipContext):

    def __init__(self, fieldsToExclude = None):
        super(HangarContext, self).__init__(TOOLTIP_COMPONENT.HANGAR, fieldsToExclude)
        self._slotIdx = 0
        self._vehicle = None
        self._historicalBattleID = -1
        return

    def getVehicle(self):
        return g_currentVehicle.item

    def buildItem(self, intCD, slotIdx = 0, historicalBattleID = -1):
        self._slotIdx = int(slotIdx)
        self._vehicle = self.getVehicle()
        self._historicalBattleID = historicalBattleID
        return g_itemsCache.items.getItemByCD(int(intCD))

    def getStatusConfiguration(self, item):
        value = super(HangarContext, self).getStatusConfiguration(item)
        inventoryCheck = item.itemTypeID in GUI_ITEM_TYPE.VEHICLE_MODULES
        isInInventory = inventoryCheck and item.isInInventory
        value.checkBuying = not item.isInstalled(self._vehicle, self._slotIdx) and not isInInventory
        value.vehicle = self._vehicle
        value.slotIdx = self._slotIdx
        return value

    def getStatsConfiguration(self, item):
        value = super(HangarContext, self).getStatsConfiguration(item)
        value.unlockPrice = not item.isUnlocked
        if item.itemTypeID == GUI_ITEM_TYPE.VEHICLE:
            value.buyPrice = not item.isInInventory
        else:
            value.buyPrice = not item.isInstalled(self._vehicle, self._slotIdx)
        value.xp = True
        value.dailyXP = True
        value.vehicle = self._vehicle
        value.slotIdx = self._slotIdx
        return value

    def getParamsConfiguration(self, item):
        value = super(HangarContext, self).getParamsConfiguration(item)
        value.params = gui.GUI_SETTINGS.technicalInfo
        value.vehicle = self._vehicle
        value.historicalBattleID = self._historicalBattleID
        return value


class PreviewContext(HangarContext):

    def getVehicle(self):
        return g_currentPreviewVehicle.item


class VehCmpConfigurationContext(HangarContext):

    def getVehicle(self):
        return _getCmpVehicle()


class TankmanHangarContext(HangarContext):

    def buildItem(self, invID):
        return g_itemsCache.items.getTankman(int(invID))


class TechTreeContext(ShopContext):

    def __init__(self, fieldsToExclude = None):
        super(TechTreeContext, self).__init__(fieldsToExclude)
        self._vehicle = None
        self._node = None
        return

    def buildItem(self, node, parentCD):
        self._vehicle = g_itemsCache.items.getItemByCD(int(parentCD))
        self._node = node
        return g_itemsCache.items.getItemByCD(int(node.id))

    def getStatusConfiguration(self, item):
        value = super(TechTreeContext, self).getStatusConfiguration(item)
        value.checkBuying = not item.isInstalled(self._vehicle) and not item.isInInventory
        value.vehicle = self._vehicle
        value.node = self._node
        value.isResearchPage = True
        return value

    def getStatsConfiguration(self, item):
        value = super(TechTreeContext, self).getStatsConfiguration(item)
        value.inventoryCount = False
        value.vehiclesCount = False
        value.vehicle = self._vehicle
        value.node = self._node
        value.xp = True
        return value

    def getParamsConfiguration(self, item):
        value = super(TechTreeContext, self).getParamsConfiguration(item)
        value.vehicle = self._vehicle
        return value


class VehCmpModulesContext(TechTreeContext):

    def buildItem(self, node, parentCD):
        self._vehicle = _getCmpVehicle()
        self._node = node
        return g_itemsCache.items.getItemByCD(int(node.id))

    def getStatusConfiguration(self, item):
        value = super(TechTreeContext, self).getStatusConfiguration(item)
        value.isResearchPage = False
        value.showCustomStates = False
        value.checkBuying = False
        return value


class TechMainContext(HangarContext):

    def __init__(self, fieldsToExclude = None):
        super(TechMainContext, self).__init__(fieldsToExclude)
        self._eqs = tuple()

    def buildItem(self, compact, slotIdx = 0, eqs = None):
        if eqs is not None:
            self._eqs = eqs
        return super(TechMainContext, self).buildItem(compact, slotIdx=slotIdx)

    def getStatusConfiguration(self, item):
        value = super(TechMainContext, self).getStatusConfiguration(item)
        value.eqs = self._eqs
        value.checkBuying = True
        return value

    def getStatsConfiguration(self, item):
        value = super(TechMainContext, self).getStatsConfiguration(item)
        value.buyPrice = True
        return value


class PersonalCaseContext(ToolTipContext):
    """ Personal case class for tool tip context
    """

    def __init__(self, fieldsToExclude = None):
        super(PersonalCaseContext, self).__init__(TOOLTIP_COMPONENT.PERSONAL_CASE, fieldsToExclude)

    def buildItem(self, skillID, tankmanID):
        tankman = g_itemsCache.items.getTankman(int(tankmanID))
        skill = findFirst(lambda x: x.name == skillID, tankman.skills)
        if skill is None:
            skill = TankmanSkill(skillID)
        return skill


class NewSkillContext(PersonalCaseContext):
    """ Tankman skill class for tool tip context
    """
    SKILL_MOCK = namedtuple('SkillMock', ('header', 'userName', 'shortDescription', 'description', 'count', 'level'))

    def buildItem(self, tankmanID):
        tankman = g_itemsCache.items.getTankman(int(tankmanID))
        skillsCount, lastSkillLevel = (0, 0)
        if tankman is not None:
            skillsCount, lastSkillLevel = tankman.newSkillCount
        header = text_styles.main(TOOLTIPS.BUYSKILL_HEADER)
        if skillsCount > 1 or lastSkillLevel > 0:
            header = text_styles.highTitle(TOOLTIPS.BUYSKILL_HEADER)
        return self.SKILL_MOCK(header, makeString('#tooltips:personal_case/skills/new/header'), makeString('#tooltips:personal_case/skills/new/body'), makeString('#tooltips:personal_case/skills/new/body'), skillsCount, lastSkillLevel)


class ProfileContext(ToolTipContext):
    """ Profile class for tool tip context
    """

    def __init__(self, fieldsToExclude = None):
        super(ProfileContext, self).__init__(TOOLTIP_COMPONENT.PROFILE, fieldsToExclude)
        self._dossier = None
        self._dossierType = None
        self._isCurrentUserDossier = True
        return

    def buildItem(self, dossierType, dossierCompDescr, block, name, isRare, isCurrentUserDossier):
        dossier = loadDossier(dossierCompDescr)
        if dossierType == constants.DOSSIER_TYPE.VEHICLE:
            self._component = TOOLTIP_COMPONENT.PROFILE_VEHICLE
        self._dossier = dossier
        self._dossierType = dossierType
        self._isCurrentUserDossier = isCurrentUserDossier
        if block == ACHIEVEMENT_BLOCK.RARE:
            name = int(name)
        return dossier.getTotalStats().getAchievement((block, name))

    def getParamsConfiguration(self, item):
        value = super(ProfileContext, self).getParamsConfiguration(item)
        value.dossier = self._dossier
        value.dossierType = self._dossierType
        value.isCurrentUserDossier = self._isCurrentUserDossier
        return value


class BattleResultContext(ProfileContext):
    """ Profile class for tool tip context
    """

    def __init__(self, fieldsToExclude = None):
        super(BattleResultContext, self).__init__(fieldsToExclude)
        self._component = TOOLTIP_COMPONENT.PROFILE

    def buildItem(self, block, name, value = 0, customData = None):
        factory = factories.getAchievementFactory((block, name))
        if factory is not None:
            return factory.create(value=value)
        else:
            return

    def getParamsConfiguration(self, item):
        value = super(ProfileContext, self).getParamsConfiguration(item)
        value.checkAchievementExistence = False
        return value


class BattleResultMarksOnGunContext(BattleResultContext):

    def buildItem(self, block, name, value = 0, customData = None):
        item = super(BattleResultMarksOnGunContext, self).buildItem(block, name, value, customData)
        if item is not None and customData is not None:
            damageRating, vehNationID = customData
            item.setVehicleNationID(vehNationID)
            item.setDamageRating(damageRating)
            return item
        else:
            return


class BattleResultMarkOfMasteryContext(BattleResultContext):

    def buildItem(self, block, name, value = 0, customData = None):
        item = super(BattleResultMarkOfMasteryContext, self).buildItem(block, name, value, customData)
        if item is not None and customData is not None:
            prevMarkOfMastery, compDescr = customData
            item.setPrevMarkOfMastery(prevMarkOfMastery)
            item.setCompDescr(compDescr)
        return item


class FinalStatisticContext(ToolTipContext):
    """ Final statistic class for tool tip context
    """

    def __init__(self, fieldsToExclude = None):
        super(FinalStatisticContext, self).__init__(TOOLTIP_COMPONENT.FINAL_STATISTIC, fieldsToExclude)


class CyberSportUnitContext(ToolTipContext):
    """ Final statistic class for tool tip context
    """

    def __init__(self, fieldsToExclude = None):
        super(CyberSportUnitContext, self).__init__(TOOLTIP_COMPONENT.CYBER_SPORT_UNIT, fieldsToExclude)


class FortificationContext(ToolTipContext):
    """ Fortification class for tool tip context
    """

    def __init__(self, fieldsToExclude = None):
        super(FortificationContext, self).__init__(TOOLTIP_COMPONENT.FORTIFICATIONS, fieldsToExclude)


class ReserveContext(ToolTipContext):
    """ Reserve class for tool tip context
    """

    def __init__(self, fieldsToExclude = None):
        super(ReserveContext, self).__init__(TOOLTIP_COMPONENT.RESERVE, fieldsToExclude)


class ClanProfileFortBuildingContext(ToolTipContext):
    """ Clan profile fort building class for tool tip context
    """

    def __init__(self, fieldsToExclude = None):
        super(ClanProfileFortBuildingContext, self).__init__(TOOLTIP_COMPONENT.CLAN_PROFILE, fieldsToExclude)


class CustomizationContext(ToolTipContext):
    """ Customization class for tool tip context
    """

    def __init__(self, fieldsToExclude = None):
        super(CustomizationContext, self).__init__(TOOLTIP_COMPONENT.CUSTOMIZATION, fieldsToExclude)

    def buildItem(self, nationId, itemId, customizationType):
        if customizationType == CUSTOMIZATION_ITEM_TYPE.CAMOUFLAGE:
            result = vehicles.g_cache.customization(nationId)['camouflages'][itemId]
        elif customizationType == CUSTOMIZATION_ITEM_TYPE.EMBLEM:
            emblemGroups, emblems, _ = vehicles.g_cache.playerEmblems()
            emblem = emblems[itemId]
            allow, deny = emblemGroups.get(emblem[0])[4:]
            result = list(emblem)
            result.extend([allow, deny])
        elif customizationType == CUSTOMIZATION_ITEM_TYPE.INSCRIPTION:
            customizationData = vehicles.g_cache.customization(nationId)
            inscriptionGroups = customizationData.get('inscriptionGroups', {})
            inscription = customizationData.get('inscriptions', {}).get(itemId)
            allow, deny = inscriptionGroups.get(inscription[0])[3:]
            result = list(inscription)
            result.extend([allow, deny])
        else:
            result = None
        return result


class ContactContext(ToolTipContext):
    """ Contact class for tool tip context
    """

    def __init__(self, fieldsToExclude = None):
        super(ContactContext, self).__init__(TOOLTIP_COMPONENT.CONTACT, fieldsToExclude)


class FortOrderContext(FortificationContext):
    """ Fortification class for tool tip context
    """

    def buildItem(self, fortOrderTypeID, level):
        return FortOrder(int(fortOrderTypeID), level=int(level))


class BattleConsumableContext(FortificationContext):
    """ Context for all battle consumables.
    """

    def buildItem(self, intCD):
        return g_itemsCache.items.getItemByCD(int(intCD))


class HangarTutorialContext(ToolTipContext):
    """ Hangar tutorial class for tool tip context
    """

    def __init__(self, fieldsToExclude = None):
        super(HangarTutorialContext, self).__init__(TOOLTIP_COMPONENT.HANGAR_TUTORIAL, fieldsToExclude)


class FortSortieLimitContext(FortificationContext):
    """ Fortifications sorties limit class for tool tip context
    """
    pass


class FortPopoverDefResProgressContext(FortificationContext):
    """ Fortifications popover defRes progress limit class for tool tip context
    """
    pass


class SettingsMinimapContext(ToolTipContext):
    pass


class SquadRestrictionContext(ToolTipContext):
    pass


class TechCustomizationContext(ToolTipContext):

    def __init__(self, fieldsToExclude = None):
        super(TechCustomizationContext, self).__init__(TOOLTIP_COMPONENT.TECH_CUSTOMIZATION, fieldsToExclude)


class BoosterContext(ToolTipContext):
    """ Booster class for tooltip context
    """

    def __init__(self, fieldsToExclude = None):
        super(BoosterContext, self).__init__(TOOLTIP_COMPONENT.BOOSTER, fieldsToExclude)

    def getStatsConfiguration(self, booster):
        return BoosterStatsConfiguration()

    def buildItem(self, boosterID):
        return g_goodiesCache.getBooster(boosterID)


class ShopBoosterContext(BoosterContext):

    def getStatsConfiguration(self, booster):
        value = super(ShopBoosterContext, self).getStatsConfiguration(booster)
        value.buyPrice = True
        return value


class QuestsBoosterContext(BoosterContext):

    def getStatsConfiguration(self, booster):
        value = super(QuestsBoosterContext, self).getStatsConfiguration(booster)
        value.quests = True
        return value


class BoosterStatsConfiguration(object):
    __slots__ = ('buyPrice', 'quests', 'activeState')

    def __init__(self):
        self.buyPrice = False
        self.quests = False
        self.activeState = True


class HangarServerStatusContext(ToolTipContext):
    """ Hangar server status context
    """

    def __init__(self, fieldsToExclude = None):
        super(HangarServerStatusContext, self).__init__(TOOLTIP_COMPONENT.HANGAR, fieldsToExclude)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\shared\tooltips\contexts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:52:43 St�edn� Evropa (b�n� �as)
