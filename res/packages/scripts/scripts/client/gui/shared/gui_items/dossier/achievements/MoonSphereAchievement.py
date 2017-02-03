# 2017.02.03 21:52:26 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/MoonSphereAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import RegularAchievement
from abstract.mixins import NoProgressBar
from gui.shared.gui_items.dossier.achievements import validators

class MoonSphereAchievement(RegularAchievement, NoProgressBar):

    def __init__(self, dossier, value = None):
        super(MoonSphereAchievement, self).__init__('moonSphere', _AB.SINGLE, dossier, value)

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.alreadyAchieved(cls, name, block, dossier)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\MoonSphereAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:52:26 St�edn� Evropa (b�n� �as)
