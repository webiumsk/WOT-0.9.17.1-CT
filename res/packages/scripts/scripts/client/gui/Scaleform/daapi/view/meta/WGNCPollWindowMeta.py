# 2017.02.03 21:51:11 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/WGNCPollWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class WGNCPollWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onBtnClick(self):
        self._printOverrideError('onBtnClick')

    def onLinkClick(self, actions):
        self._printOverrideError('onLinkClick')

    def as_setWindowTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)

    def as_setTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setText(value)

    def as_setButtonLblS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonLbl(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\WGNCPollWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:51:11 St�edn� Evropa (b�n� �as)
