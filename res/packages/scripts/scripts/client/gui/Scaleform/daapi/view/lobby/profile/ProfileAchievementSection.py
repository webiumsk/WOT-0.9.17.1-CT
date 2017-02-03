# 2017.02.03 21:50:17 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileAchievementSection.py
from gui.Scaleform.daapi.view.meta.ProfileAchievementSectionMeta import ProfileAchievementSectionMeta
from gui.shared.utils.RareAchievementsCache import g_rareAchievesCache

class ProfileAchievementSection(ProfileAchievementSectionMeta):

    def __init__(self, *args):
        super(ProfileAchievementSection, self).__init__(*args)
        g_rareAchievesCache.onImageReceived += self._onRareImageReceived

    def _onRareImageReceived(self, imgType, rareID, imageData):
        pass

    def _disposeRequester(self):
        g_rareAchievesCache.onImageReceived -= self._onRareImageReceived
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\profile\ProfileAchievementSection.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:17 Støední Evropa (bìžný èas)
