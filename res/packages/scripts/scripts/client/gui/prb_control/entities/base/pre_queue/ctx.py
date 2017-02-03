# 2017.02.03 21:48:32 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/base/pre_queue/ctx.py
from gui.prb_control.entities.base.ctx import PrbCtrlRequestCtx, LeavePrbAction
from gui.prb_control.settings import CTRL_ENTITY_TYPE, REQUEST_TYPE
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared.utils.decorators import ReprInjector

class _PreQueueRequestCtx(PrbCtrlRequestCtx):
    """
    Base pre queue request context.
    """

    def __init__(self, **kwargs):
        super(_PreQueueRequestCtx, self).__init__(ctrlType=CTRL_ENTITY_TYPE.PREQUEUE, **kwargs)


class QueueCtx(_PreQueueRequestCtx):
    """
    Enter queue request context.
    """

    def getRequestType(self):
        return REQUEST_TYPE.QUEUE


class DequeueCtx(_PreQueueRequestCtx):
    """
    Leave queue request context.
    """

    def getRequestType(self):
        return REQUEST_TYPE.DEQUEUE


class JoinPreQueueModeCtx(_PreQueueRequestCtx):
    """
    Join pre queue request context.
    """

    def __init__(self, queueType, flags = FUNCTIONAL_FLAG.UNDEFINED, waitingID = ''):
        super(JoinPreQueueModeCtx, self).__init__(entityType=queueType, flags=flags, waitingID=waitingID)

    def getID(self):
        """
        Stub to look like other join mode ctx.
        """
        return 0


@ReprInjector.withParent(('getWaitingID', 'waitingID'))

class LeavePreQueueCtx(_PreQueueRequestCtx):
    """
    Leave pre queue request context.
    """

    def getRequestType(self):
        return REQUEST_TYPE.LEAVE
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\base\pre_queue\ctx.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:32 St�edn� Evropa (b�n� �as)
