# 2017.02.03 21:51:09 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TutorialLoadingMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TutorialLoadingMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_setTutorialArenaInfoS(self, data):
        """
        :param data: Represented by DAAPIArenaInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTutorialArenaInfo(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\TutorialLoadingMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:51:09 St�edn� Evropa (b�n� �as)
