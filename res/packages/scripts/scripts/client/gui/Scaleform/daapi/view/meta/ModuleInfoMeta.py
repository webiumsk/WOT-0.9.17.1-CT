# 2017.02.03 21:51:01 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ModuleInfoMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ModuleInfoMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onCancelClick(self):
        self._printOverrideError('onCancelClick')

    def onActionButtonClick(self):
        self._printOverrideError('onActionButtonClick')

    def as_setModuleInfoS(self, moduleInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setModuleInfo(moduleInfo)

    def as_setActionButtonS(self, data):
        """
        :param data: Represented by ModuleInfoActionVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setActionButton(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ModuleInfoMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:51:01 St�edn� Evropa (b�n� �as)
