# 2017.02.03 21:49:56 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/FortSortieOrdersPanelComponent.py
import UnitBase
from gui.Scaleform.genConsts.FORTIFICATION_ALIASES import FORTIFICATION_ALIASES
from gui.Scaleform.daapi.view.lobby.fortifications.FortBattleRoomOrdersPanelComponent import FortBattleRoomOrdersPanelComponent

class FortSortieOrdersPanelComponent(FortBattleRoomOrdersPanelComponent):

    def _isConsumablesAvailable(self):
        _, unit = self.prbEntity.getUnit(self.prbEntity.getUnitIdx())
        return unit is not None and unit.getRosterTypeID() == UnitBase.ROSTER_TYPE.SORTIE_ROSTER_10

    def _getSlotsProps(self):
        props = super(FortSortieOrdersPanelComponent, self)._getSlotsProps()
        props.update({'panelAlias': FORTIFICATION_ALIASES.FORT_SORTIE_ORDERS_PANEL_COMPONENT_ALIAS})
        return props
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\fortifications\FortSortieOrdersPanelComponent.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:49:56 St�edn� Evropa (b�n� �as)
