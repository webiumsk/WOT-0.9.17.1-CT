# 2017.02.03 21:50:47 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleResultsMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BattleResultsMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def saveSorting(self, iconType, sortDirection, bonusType):
        self._printOverrideError('saveSorting')

    def showEventsWindow(self, questID, eventType):
        self._printOverrideError('showEventsWindow')

    def getClanEmblem(self, uid, clanID):
        self._printOverrideError('getClanEmblem')

    def onResultsSharingBtnPress(self):
        self._printOverrideError('onResultsSharingBtnPress')

    def showUnlockWindow(self, itemId, unlockType):
        self._printOverrideError('showUnlockWindow')

    def as_setDataS(self, data):
        """
        :param data: Represented by BattleResultsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setClanEmblemS(self, uid, iconTag):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(uid, iconTag)

    def as_setTeamInfoS(self, uid, iconTag, teamName):
        if self._isDAAPIInited():
            return self.flashObject.as_setTeamInfo(uid, iconTag, teamName)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BattleResultsMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:47 Støední Evropa (bìžný èas)
