# 2017.02.03 21:58:51 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/idlelib/Delegator.py


class Delegator:

    def __init__(self, delegate = None):
        self.delegate = delegate
        self.__cache = set()

    def __getattr__(self, name):
        attr = getattr(self.delegate, name)
        setattr(self, name, attr)
        self.__cache.add(name)
        return attr

    def resetcache(self):
        for key in self.__cache:
            try:
                delattr(self, key)
            except AttributeError:
                pass

        self.__cache.clear()

    def setdelegate(self, delegate):
        self.resetcache()
        self.delegate = delegate
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\Lib\idlelib\Delegator.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:58:51 St�edn� Evropa (b�n� �as)
