# 2017.02.03 21:50:45 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AwardWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class AwardWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onOKClick(self):
        self._printOverrideError('onOKClick')

    def onTakeNextClick(self):
        self._printOverrideError('onTakeNextClick')

    def onCloseClick(self):
        self._printOverrideError('onCloseClick')

    def as_setDataS(self, data):
        """
        :param data: Represented by AwardWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\AwardWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:45 St�edn� Evropa (b�n� �as)
