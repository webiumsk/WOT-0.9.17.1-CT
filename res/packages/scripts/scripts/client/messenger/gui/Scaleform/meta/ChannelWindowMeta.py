# 2017.02.03 21:53:31 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ChannelWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ChannelWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def showFAQWindow(self):
        self._printOverrideError('showFAQWindow')

    def getClientID(self):
        self._printOverrideError('getClientID')

    def as_setTitleS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(title)

    def as_setCloseEnabledS(self, enabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setCloseEnabled(enabled)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\messenger\gui\Scaleform\meta\ChannelWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:53:31 St�edn� Evropa (b�n� �as)
