# 2017.02.03 21:51:07 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SmartPopOverViewMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractPopOverView import AbstractPopOverView

class SmartPopOverViewMeta(AbstractPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractPopOverView
    """

    def as_setPositionKeyPointS(self, valX, valY):
        if self._isDAAPIInited():
            return self.flashObject.as_setPositionKeyPoint(valX, valY)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\SmartPopOverViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:51:07 St�edn� Evropa (b�n� �as)
