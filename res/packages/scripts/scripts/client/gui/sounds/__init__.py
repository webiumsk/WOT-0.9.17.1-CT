# 2017.02.03 21:53:00 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/sounds/__init__.py
from gui.sounds.sounds_ctrl import SoundsController
from skeletons.gui.sounds import ISoundsController
__all__ = ('getSoundsConfig',)

def getSoundsConfig(manager):
    """ Configures services for package sounds.
    :param manager: helpers.dependency.DependencyManager
    """
    ctrl = SoundsController()
    ctrl.init()
    manager.bindInstance(ISoundsController, ctrl, finalizer='fini')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\sounds\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:53:00 St�edn� Evropa (b�n� �as)
