# 2017.02.03 21:50:46 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseRallyViewMeta.py
from gui.Scaleform.daapi.view.lobby.rally.AbstractRallyView import AbstractRallyView

class BaseRallyViewMeta(AbstractRallyView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractRallyView
    """

    def as_setCoolDownS(self, value, requestId):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDown(value, requestId)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BaseRallyViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:46 St�edn� Evropa (b�n� �as)
