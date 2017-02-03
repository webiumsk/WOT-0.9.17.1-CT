# 2017.02.03 21:52:27 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/ReliableComradeAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SimpleProgressAchievement

class ReliableComradeAchievement(SimpleProgressAchievement):

    def __init__(self, dossier, value = None):
        super(ReliableComradeAchievement, self).__init__('reliableComrade', _AB.TOTAL, dossier, value)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, 'reliableComradeSeries')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\ReliableComradeAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:52:28 Støední Evropa (bìžný èas)
