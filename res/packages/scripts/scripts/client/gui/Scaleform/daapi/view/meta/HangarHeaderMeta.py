# 2017.02.03 21:50:59 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/HangarHeaderMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class HangarHeaderMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def showCommonQuests(self):
        self._printOverrideError('showCommonQuests')

    def showPersonalQuests(self):
        self._printOverrideError('showPersonalQuests')

    def showBeginnerQuests(self):
        self._printOverrideError('showBeginnerQuests')

    def as_setDataS(self, data):
        """
        :param data: Represented by HangarHeaderVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\HangarHeaderMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:59 St�edn� Evropa (b�n� �as)
