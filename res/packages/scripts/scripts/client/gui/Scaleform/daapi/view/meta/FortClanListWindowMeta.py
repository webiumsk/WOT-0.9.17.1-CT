# 2017.02.03 21:50:55 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortClanListWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortClanListWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def as_setDataS(self, data):
        """
        :param data: Represented by FortClanListWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FortClanListWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:55 St�edn� Evropa (b�n� �as)
