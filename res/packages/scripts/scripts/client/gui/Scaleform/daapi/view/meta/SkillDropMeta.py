# 2017.02.03 21:51:07 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SkillDropMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SkillDropMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def calcDropSkillsParams(self, tmanCompDescr, xpReuseFraction):
        self._printOverrideError('calcDropSkillsParams')

    def dropSkills(self, dropSkillCostIdx):
        self._printOverrideError('dropSkills')

    def as_setDataS(self, data):
        """
        :param data: Represented by SkillDropModel (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setGoldS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setGold(value)

    def as_setCreditsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCredits(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\SkillDropMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:51:07 St�edn� Evropa (b�n� �as)
