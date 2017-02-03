# 2017.02.03 21:48:22 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/miniclient/invitations/pointcuts.py
from helpers import aop
import aspects

class PrbDisableAcceptButton(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.prb_control.invites', 'InvitesManager', 'canAcceptInvite', aspects=(aspects.DisableAccept,))


class PrbInvitationText(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.prb_control.formatters.invites', 'PrbInviteHtmlTextFormatter', 'getNote', aspects=(aspects.InvitationNote,))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\miniclient\invitations\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:22 St�edn� Evropa (b�n� �as)
