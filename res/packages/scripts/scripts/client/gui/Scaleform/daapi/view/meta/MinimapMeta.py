# 2017.02.03 21:51:01 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MinimapMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MinimapMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def setAttentionToCell(self, x, y, isRightClick):
        self._printOverrideError('setAttentionToCell')

    def applyNewSize(self, sizeIndex):
        self._printOverrideError('applyNewSize')

    def as_setSizeS(self, size):
        if self._isDAAPIInited():
            return self.flashObject.as_setSize(size)

    def as_setVisibleS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(isVisible)

    def as_setAlphaS(self, alpha):
        if self._isDAAPIInited():
            return self.flashObject.as_setAlpha(alpha)

    def as_showVehiclesNameS(self, visibility):
        if self._isDAAPIInited():
            return self.flashObject.as_showVehiclesName(visibility)

    def as_setBackgroundS(self, path):
        if self._isDAAPIInited():
            return self.flashObject.as_setBackground(path)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\MinimapMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:51:01 St�edn� Evropa (b�n� �as)
