# 2017.02.03 21:52:28 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/TankwomenAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SimpleProgressAchievement

class TankwomenAchievement(SimpleProgressAchievement):

    def __init__(self, dossier, value = None):
        super(TankwomenAchievement, self).__init__('tankwomen', _AB.SINGLE, dossier, value)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, 'tankwomenProgress')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\TankwomenAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:52:28 St�edn� Evropa (b�n� �as)
