# 2017.02.03 21:50:47 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleSessionListMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BattleSessionListMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def requestToJoinTeam(self, prbID, prbType):
        self._printOverrideError('requestToJoinTeam')

    def getClientID(self):
        self._printOverrideError('getClientID')

    def as_refreshListS(self, data):
        """
        :param data: Represented by DataProvider (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_refreshList(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BattleSessionListMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:47 St�edn� Evropa (b�n� �as)
