# 2017.02.03 21:52:24 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/ForTacticalOperationsAchievement.py
from abstract import ClassProgressAchievement
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB

class ForTacticalOperationsAchievement(ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        super(ForTacticalOperationsAchievement, self).__init__('forTacticalOperations', _AB.TEAM_7X7, dossier, value)

    def getNextLevelInfo(self):
        return ('winsLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, 'forTacticalOperations')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getTeam7x7Stats().getWinsCount()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\ForTacticalOperationsAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:52:24 St�edn� Evropa (b�n� �as)
