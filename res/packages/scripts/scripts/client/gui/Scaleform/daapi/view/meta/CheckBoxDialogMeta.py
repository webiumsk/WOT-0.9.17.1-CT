# 2017.02.03 21:50:48 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CheckBoxDialogMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class CheckBoxDialogMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def onCheckBoxChange(self, isSelected):
        self._printOverrideError('onCheckBoxChange')

    def as_setCheckBoxLabelS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCheckBoxLabel(value)

    def as_setCheckBoxSelectedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCheckBoxSelected(value)

    def as_setCheckBoxEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCheckBoxEnabled(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\CheckBoxDialogMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:48 St�edn� Evropa (b�n� �as)
