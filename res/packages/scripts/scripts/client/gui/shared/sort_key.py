# 2017.02.03 21:52:10 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/sort_key.py


class SortKey(object):
    __slots__ = ()

    def __lt__(self, other):
        return self._cmp(other) < 0

    def __gt__(self, other):
        return self._cmp(other) > 0

    def __eq__(self, other):
        return self._cmp(other) == 0

    def __le__(self, other):
        return self._cmp(other) <= 0

    def __ge__(self, other):
        return self._cmp(other) >= 0

    def __ne__(self, other):
        return self._cmp(other) != 0

    def __hash__(self):
        raise TypeError('hash not implemented')

    def _cmp(self, other):
        raise NotImplementedError
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\shared\sort_key.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:52:10 Støední Evropa (bìžný èas)
