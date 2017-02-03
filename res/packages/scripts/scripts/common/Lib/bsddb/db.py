# 2017.02.03 21:57:21 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/bsddb/db.py
import sys
absolute_import = sys.version_info[0] >= 3
if not absolute_import:
    if __name__.startswith('bsddb3.'):
        from _pybsddb import *
        from _pybsddb import __version__
    else:
        from _bsddb import *
        from _bsddb import __version__
elif __name__.startswith('bsddb3.'):
    exec 'from ._pybsddb import *'
    exec 'from ._pybsddb import __version__'
else:
    exec 'from ._bsddb import *'
    exec 'from ._bsddb import __version__'
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\Lib\bsddb\db.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:57:21 Støední Evropa (bìžný èas)
