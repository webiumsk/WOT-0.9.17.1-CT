# 2017.02.03 21:48:55 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/prb_control/storages/__init__.py
from constants import PREBATTLE_TYPE as _P_TYPE
from constants import QUEUE_TYPE as _Q_TYPE
from constants import PREBATTLE_TYPE_NAMES as _P_NAMES
from constants import QUEUE_TYPE_NAMES as _Q_NAMES
from gui.prb_control.settings import CTRL_ENTITY_TYPE as _C_TYPE
from gui.prb_control.settings import CTRL_ENTITY_TYPE_NAMES as _C_NAMES
from gui.prb_control.storages.fallout_storage import FalloutLocalStorage
from gui.prb_control.storages.local_storage import LocalStorage
from gui.prb_control.storages.prb_storage import TrainingStorage
from gui.prb_control.storages.sandbox_storage import SandboxStorage
from helpers.ro_property import ROPropertyMeta
__all__ = ('legacy_storage_getter', 'prequeue_storage_getter', 'PrbStorageDecorator')

def _makeUniqueName(ctrlName, entityName):
    return '{}_{}'.format(ctrlName, entityName)


def _makeQueueName(queueType):
    if queueType not in _Q_NAMES:
        raise ValueError('Queue type is invalid {}'.format(queueType))
    return _makeUniqueName(_C_NAMES[_C_TYPE.PREQUEUE], _Q_NAMES[queueType])


def _makeLegacyName(legacyType):
    if legacyType not in _P_TYPE.LEGACY_PREBATTLES:
        raise ValueError('Legacy type is invalid {}'.format(legacyType))
    return _makeUniqueName(_C_NAMES[_C_TYPE.LEGACY], _P_NAMES[legacyType])


_PRB_STORAGE = {_makeLegacyName(_P_TYPE.TRAINING): TrainingStorage(),
 _makeQueueName(_Q_TYPE.FALLOUT): FalloutLocalStorage(),
 _makeQueueName(_Q_TYPE.SANDBOX): SandboxStorage()}

class _storage_getter(object):

    def __init__(self, name):
        super(_storage_getter, self).__init__()
        if name not in _PRB_STORAGE:
            raise ValueError('Storage "{}" not found'.format(name))
        self.__name = name

    def __call__(self, *args):
        return _PRB_STORAGE[self.__name]


class legacy_storage_getter(_storage_getter):

    def __init__(self, legacyType):
        super(legacy_storage_getter, self).__init__(_makeLegacyName(legacyType))


class prequeue_storage_getter(_storage_getter):

    def __init__(self, queueType):
        super(prequeue_storage_getter, self).__init__(_makeQueueName(queueType))


class PrbStorageDecorator(LocalStorage):
    __metaclass__ = ROPropertyMeta
    __readonly__ = _PRB_STORAGE

    def init(self):
        for storage in self.__readonly__.itervalues():
            storage.init()

    def fini(self):
        for storage in self.__readonly__.itervalues():
            storage.fini()

    def swap(self):
        for storage in self.__readonly__.itervalues():
            storage.swap()

    def clear(self):
        for storage in self.__readonly__.itervalues():
            storage.clear()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\prb_control\storages\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:55 St�edn� Evropa (b�n� �as)
