# 2017.02.03 21:50:54 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutTankCarouselMeta.py
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.tank_carousel import TankCarousel

class FalloutTankCarouselMeta(TankCarousel):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends TankCarousel
    """

    def changeVehicle(self, id):
        self._printOverrideError('changeVehicle')

    def clearSlot(self, vehicleId):
        self._printOverrideError('clearSlot')

    def shiftSlot(self, vehicleId):
        self._printOverrideError('shiftSlot')

    def as_setMultiselectionInfoS(self, data):
        """
        :param data: Represented by MultiselectionInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMultiselectionInfo(data)

    def as_getMultiselectionDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getMultiselectionDP()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FalloutTankCarouselMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:54 St�edn� Evropa (b�n� �as)
