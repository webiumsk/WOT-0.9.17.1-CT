# 2017.02.03 21:50:54 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FittingSelectPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FittingSelectPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def setVehicleModule(self, newId, oldId, isRemove):
        self._printOverrideError('setVehicleModule')

    def showModuleInfo(self, moduleId):
        self._printOverrideError('showModuleInfo')

    def as_updateS(self, data):
        """
        :param data: Represented by FittingSelectPopoverVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FittingSelectPopoverMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:54 St�edn� Evropa (b�n� �as)
