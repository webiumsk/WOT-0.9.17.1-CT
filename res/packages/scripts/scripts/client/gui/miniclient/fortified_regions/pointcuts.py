# 2017.02.03 21:48:21 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/miniclient/fortified_regions/pointcuts.py
import aspects
from helpers import aop

class OnViewPopulate(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.fortifications.components.FortWelcomeInfoView', 'FortWelcomeInfoView', '_populate', aspects=(aspects.OnViewPopulate,))


class OnFortifiedRegionsOpen(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.fortifications.FortificationsView', 'FortificationsView', 'loadView', aspects=(aspects.OnFortifiedRegionsOpen,))


class FortificationsViewSubscriptions(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.fortifications.FortificationsView', 'FortificationsView', 'onClientStateChanged', aspects=(aop.DummyAspect,))


class OnFortRequirementsUpdate(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.fortifications.components.FortWelcomeViewComponent', 'FortWelcomeViewComponent', '_FortWelcomeViewComponent__updateViewState|onClientStateChangedonClanMembersListChanged|onNavigate', aspects=(aop.DummyAspect,))


class OnSetWarningText(aop.Pointcut):
    """
    WOTD-59268
    Unnecessary warning when fortification is already created.
    Decided to disable method which sets warning text.
    """

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.meta.FortWelcomeInfoViewMeta', 'FortWelcomeInfoViewMeta', 'as_setWarningTextS', aspects=(aop.DummyAspect,))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\miniclient\fortified_regions\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:21 St�edn� Evropa (b�n� �as)
