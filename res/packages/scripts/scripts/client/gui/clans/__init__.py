# 2017.02.03 21:48:06 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/clans/__init__.py
from skeletons.gui.clans import IClanController
__all__ = ('getClanServicesConfig',)

def getClanServicesConfig(manager):
    """ Configures services for package clans.
    :param manager: helpers.dependency.DependencyManager
    """
    from gui.clans.clan_controller import ClanController
    ctrl = ClanController()
    ctrl.init()
    manager.bindInstance(IClanController, ctrl, finalizer='fini')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\clans\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:06 Støední Evropa (bìžný èas)
