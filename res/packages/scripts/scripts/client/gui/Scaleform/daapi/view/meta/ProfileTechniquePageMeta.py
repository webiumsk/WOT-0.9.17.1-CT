# 2017.02.03 21:51:03 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileTechniquePageMeta.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileTechnique import ProfileTechnique

class ProfileTechniquePageMeta(ProfileTechnique):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ProfileTechnique
    """

    def setIsInHangarSelected(self, value):
        self._printOverrideError('setIsInHangarSelected')

    def as_setSelectedVehicleIntCDS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedVehicleIntCD(index)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ProfileTechniquePageMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:51:03 St�edn� Evropa (b�n� �as)
