# 2017.02.03 21:48:24 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/miniclient/notifications/clan_applications.py
from gui import makeHtmlString
from helpers import aop
from notification.settings import NOTIFICATION_BUTTON_STATE

class _ClanMultiNotifAspect(aop.Aspect):

    def atReturn(self, cd):
        original_return_options = cd.returned
        original_return_options['submit'] = NOTIFICATION_BUTTON_STATE.VISIBLE
        return original_return_options


class _BaseClanSingleNotifAspect(aop.Aspect):

    def atReturn(self, cd):
        original_return_options = cd.returned
        original_return_options['submit'] = NOTIFICATION_BUTTON_STATE.VISIBLE
        original_return_options['cancel'] = NOTIFICATION_BUTTON_STATE.VISIBLE
        return original_return_options


class _ClanSingleNotifHtmlTextFormatterAspect(aop.Aspect):

    def atReturn(self, cd):
        returned = cd.returned
        returned = makeHtmlString('html_templates:lobby/clans', 'appCommentMiniclient')
        cd.change()
        return returned


class ClanMultiNotifPointCut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'notification.decorators', '_ClanMultiDecorator', '_getButtonsStates', aspects=(_ClanMultiNotifAspect,))


class ClanSingleInviteNotifPointCut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'notification.decorators', 'ClanSingleInviteDecorator', '_getButtonsStates', aspects=(_BaseClanSingleNotifAspect,))


class ClanSingleAppNotifPointCut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'notification.decorators', 'ClanSingleAppDecorator', '_getButtonsStates', aspects=(_BaseClanSingleNotifAspect,))


class ClanSingleNotificationHtmlTextFormatterPointCut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.clans.formatters', 'ClanSingleNotificationHtmlTextFormatter', 'getComment', aspects=(_ClanSingleNotifHtmlTextFormatterAspect,))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\miniclient\notifications\clan_applications.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:24 St�edn� Evropa (b�n� �as)
