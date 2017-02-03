# 2017.02.03 21:48:23 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/miniclient/lobby/strongholds/aspects.py
from helpers import aop
from gui.Scaleform.genConsts.FORTIFICATION_ALIASES import FORTIFICATION_ALIASES
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS

class MakeStrongholdsUnavailable(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        tooltip = TOOLTIPS.HEADER_BUTTONS_FORTS_SANDBOX_TURNEDOFF
        return {'label': MENU.HEADERBUTTONS_FORTS,
         'value': FORTIFICATION_ALIASES.FORTIFICATIONS2_VIEW_ALIAS,
         'tooltip': tooltip,
         'enabled': False}
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\miniclient\lobby\strongholds\aspects.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:23 Støední Evropa (bìžný èas)
