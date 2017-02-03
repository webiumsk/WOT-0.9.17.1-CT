# 2017.02.03 21:55:29 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/dossiers2/custom/__init__.py


def init():
    from dossiers2.custom.cache import buildCache
    buildCache()
    from dossiers2.custom.dependencies import init as dependencies_init
    dependencies_init()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\dossiers2\custom\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:55:29 Støední Evropa (bìžný èas)
