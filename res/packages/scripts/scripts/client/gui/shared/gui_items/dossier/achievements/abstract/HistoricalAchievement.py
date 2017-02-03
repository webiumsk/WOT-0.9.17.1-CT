# 2017.02.03 21:52:29 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/HistoricalAchievement.py
from RegularAchievement import RegularAchievement
from mixins import HasVehiclesList, Deprecated

class HistoricalAchievement(Deprecated, HasVehiclesList, RegularAchievement):

    def getVehiclesListTitle(self):
        return 'vehiclesTakePart'

    def _getVehiclesDescrsList(self):
        return []
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\abstract\HistoricalAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:52:29 Støední Evropa (bìžný èas)
