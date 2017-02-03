# 2017.02.03 21:48:33 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/base/pre_queue/permissions.py
from gui.prb_control.entities.base.permissions import IPrbPermissions

class PreQueuePermissions(IPrbPermissions):
    """
    Persmissions class for prequeue actions.
    """

    def __init__(self, isInQueue):
        super(PreQueuePermissions, self).__init__()
        self.__isInQueue = isInQueue

    def canChangeVehicle(self):
        return not self.__isInQueue

    def canCreateSquad(self):
        return not self.__isInQueue
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\base\pre_queue\permissions.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:33 St�edn� Evropa (b�n� �as)
