# 2017.02.03 21:51:02 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PopOverViewMeta.py
from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class PopOverViewMeta(WrapperViewMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends WrapperViewMeta
    """

    def as_setArrowDirectionS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setArrowDirection(value)

    def as_setArrowPositionS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setArrowPosition(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\PopOverViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:51:02 St�edn� Evropa (b�n� �as)
