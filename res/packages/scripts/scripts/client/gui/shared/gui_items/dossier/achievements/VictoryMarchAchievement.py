# 2017.02.03 21:52:28 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/VictoryMarchAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement
from abstract.mixins import Deprecated, NoProgressBar

class VictoryMarchAchievement(Deprecated, NoProgressBar, SeriesAchievement):

    def __init__(self, dossier, value = None):
        super(VictoryMarchAchievement, self).__init__('victoryMarch', _AB.SINGLE, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.RATED_7X7, 'victoryMarchSeries'), (_AB.RATED_7X7, 'maxVictoryMarchSeries'))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\VictoryMarchAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:52:28 Støední Evropa (bìžný èas)
