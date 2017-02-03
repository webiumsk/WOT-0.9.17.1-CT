# 2017.02.03 21:52:24 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/DiehardAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement

class DiehardAchievement(SeriesAchievement):

    def __init__(self, dossier, value = None):
        super(DiehardAchievement, self).__init__('diehard', _AB.SINGLE, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, 'diehardSeries'), (_AB.TOTAL, 'maxDiehardSeries'))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\DiehardAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:52:24 St�edn� Evropa (b�n� �as)
