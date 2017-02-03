# 2017.02.03 21:48:24 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/miniclient/login/aspects.py
from helpers import aop

class ShowBGWallpaper(aop.Aspect):

    def __init__(self):
        super(ShowBGWallpaper, self).__init__()

    def atCall(self, cd):
        super(ShowBGWallpaper, self).atCall(cd)
        cd.self.showWallpaper(showSwitchButton=False)
        cd.avoid()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\miniclient\login\aspects.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:24 Støední Evropa (bìžný èas)
