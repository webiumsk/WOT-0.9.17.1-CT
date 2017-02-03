# 2017.02.03 21:46:26 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/BotPoint.py
import BigWorld
from debug_utils import LOG_DEBUG

class BotPoint(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        LOG_DEBUG('BotPoint ', self.position)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\BotPoint.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:46:26 Støední Evropa (bìžný èas)
