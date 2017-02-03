# 2017.02.03 21:51:01 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ModulesPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ModulesPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def showModuleInfo(self, moduleId):
        self._printOverrideError('showModuleInfo')

    def as_setDataS(self, data):
        """
        :param data: Represented by DevicesDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setVehicleHasTurretS(self, hasTurret):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleHasTurret(hasTurret)

    def as_setModulesEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setModulesEnabled(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ModulesPanelMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:51:01 Støední Evropa (bìžný èas)
