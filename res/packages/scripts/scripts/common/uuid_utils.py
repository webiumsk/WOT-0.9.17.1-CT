# 2017.02.03 21:55:10 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/uuid_utils.py
import os
import random
from uuid import uuid1
_node = None

def _getNode():
    global _node
    if _node is not None:
        return _node
    else:
        _node = random.randrange(0, 4294967296L) << 16
        _node = _node | os.getpid() & 65535
        _node = _node | 1099511627776L
        return _node


def genUUID():
    return uuid1(_getNode())
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\uuid_utils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:55:10 St�edn� Evropa (b�n� �as)
