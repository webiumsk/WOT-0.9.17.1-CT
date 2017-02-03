# 2017.02.03 21:46:48 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/WWISE.py
enabled = True
try:
    from _WWISE import *
    import _WWISE
except ImportError:
    print 'WARNING: WWISE support is not enabled.'
    enabled = False
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\WWISE.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:46:48 Støední Evropa (bìžný èas)
