# 2017.02.03 21:50:56 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortIntelligenceClanDescriptionMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FortIntelligenceClanDescriptionMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onOpenCalendar(self):
        self._printOverrideError('onOpenCalendar')

    def onOpenClanList(self):
        self._printOverrideError('onOpenClanList')

    def onOpenClanStatistics(self):
        self._printOverrideError('onOpenClanStatistics')

    def onOpenClanCard(self):
        self._printOverrideError('onOpenClanCard')

    def onAddRemoveFavorite(self, isAdd):
        self._printOverrideError('onAddRemoveFavorite')

    def onAttackDirection(self, uid):
        self._printOverrideError('onAttackDirection')

    def onHoverDirection(self):
        self._printOverrideError('onHoverDirection')

    def as_setDataS(self, data):
        """
        :param data: Represented by ClanDescriptionVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_updateBookMarkS(self, isAdd):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBookMark(isAdd)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FortIntelligenceClanDescriptionMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:56 St�edn� Evropa (b�n� �as)
