# 2017.02.03 22:00:12 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-irix6/CL.py
from warnings import warnpy3k
warnpy3k('the CL module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
try:
    from cl import *
except ImportError:
    from CL_old import *
else:
    del CompressImage
    del DecompressImage
    del GetAlgorithmName
    del OpenCompressor
    del OpenDecompressor
    del QueryAlgorithms
    del QueryMaxHeaderSize
    del QueryScheme
    del QuerySchemeFromName
    del SetDefault
    del SetMax
    del SetMin
    try:
        del cvt_type
    except NameError:
        pass

    del error
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\Lib\plat-irix6\CL.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 22:00:12 St�edn� Evropa (b�n� �as)
