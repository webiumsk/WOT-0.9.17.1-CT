# 2017.02.03 21:55:30 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/goodies/Goodie.py
import time
from goodie_constants import GOODIE_STATE

class Goodie(object):
    __slots__ = ['uid',
     'state',
     'expiration',
     'counter']

    def __init__(self, uid, state = GOODIE_STATE.INACTIVE, expiration = 0, counter = 0):
        self.uid = uid
        self.state = state
        self.expiration = expiration
        self.counter = counter

    def isActive(self):
        return self.state == GOODIE_STATE.ACTIVE

    def isExpired(self):
        if self.expiration and self.expiration < time.time():
            return True
        else:
            return False

    def toPdata(self):
        return (self.state, self.expiration, self.counter)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\goodies\Goodie.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:55:30 St�edn� Evropa (b�n� �as)
