# 2017.02.03 21:51:07 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SwitchPeripheryWindowMeta.py
from gui.Scaleform.daapi.view.meta.SimpleWindowMeta import SimpleWindowMeta

class SwitchPeripheryWindowMeta(SimpleWindowMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleWindowMeta
    """

    def requestForChange(self, id):
        self._printOverrideError('requestForChange')

    def onDropDownOpened(self, opened):
        self._printOverrideError('onDropDownOpened')

    def as_setServerParamsS(self, label, showDropDown):
        if self._isDAAPIInited():
            return self.flashObject.as_setServerParams(label, showDropDown)

    def as_setSelectedIndexS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedIndex(index)

    def as_getServersDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getServersDP()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\SwitchPeripheryWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:51:08 St�edn� Evropa (b�n� �as)
