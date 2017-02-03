# 2017.02.03 21:52:28 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/TacticalBreakthroughAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement

class TacticalBreakthroughAchievement(SeriesAchievement):

    def __init__(self, dossier, value = None):
        super(TacticalBreakthroughAchievement, self).__init__('tacticalBreakthrough', _AB.SINGLE, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.TEAM_7X7, 'tacticalBreakthroughSeries'), (_AB.TEAM_7X7, 'maxTacticalBreakthroughSeries'))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\TacticalBreakthroughAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:52:28 St�edn� Evropa (b�n� �as)
