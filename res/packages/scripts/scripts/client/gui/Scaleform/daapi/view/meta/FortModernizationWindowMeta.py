# 2017.02.03 21:50:57 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortModernizationWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortModernizationWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def applyAction(self):
        self._printOverrideError('applyAction')

    def openOrderDetailsWindow(self):
        self._printOverrideError('openOrderDetailsWindow')

    def as_setDataS(self, data):
        """
        :param data: Represented by BuildingModernizationVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_applyButtonLblS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_applyButtonLbl(value)

    def as_cancelButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_cancelButton(value)

    def as_windowTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_windowTitle(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FortModernizationWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:57 St�edn� Evropa (b�n� �as)
