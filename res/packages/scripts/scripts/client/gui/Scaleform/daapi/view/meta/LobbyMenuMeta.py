# 2017.02.03 21:51:00 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LobbyMenuMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class LobbyMenuMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def settingsClick(self):
        self._printOverrideError('settingsClick')

    def cancelClick(self):
        self._printOverrideError('cancelClick')

    def refuseTraining(self):
        self._printOverrideError('refuseTraining')

    def logoffClick(self):
        self._printOverrideError('logoffClick')

    def quitClick(self):
        self._printOverrideError('quitClick')

    def versionInfoClick(self):
        self._printOverrideError('versionInfoClick')

    def onCounterNeedUpdate(self):
        self._printOverrideError('onCounterNeedUpdate')

    def as_setVersionMessageS(self, data):
        """
        :param data: Represented by VersionMessageVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVersionMessage(data)

    def as_setSettingsBtnCounterS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSettingsBtnCounter(value)

    def as_removeSettingsBtnCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_removeSettingsBtnCounter()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\LobbyMenuMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:51:00 St�edn� Evropa (b�n� �as)
