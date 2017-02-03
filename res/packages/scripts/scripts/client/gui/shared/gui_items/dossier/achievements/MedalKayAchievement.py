# 2017.02.03 21:52:26 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/MedalKayAchievement.py
from abstract import ClassProgressAchievement
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB

class MedalKayAchievement(ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        super(MedalKayAchievement, self).__init__('medalKay', _AB.TOTAL, dossier, value)

    def getNextLevelInfo(self):
        return ('heroesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, 'medalKay')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, 'battleHeroes')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\MedalKayAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:52:26 St�edn� Evropa (b�n� �as)
