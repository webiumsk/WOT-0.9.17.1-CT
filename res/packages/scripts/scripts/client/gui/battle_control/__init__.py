# 2017.02.03 21:47:38 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/battle_control/__init__.py
from gui.battle_control.battle_session import BattleSessionProvider
from gui.battle_control.controllers import BattleSessionSetup
from skeletons.gui.battle_session import IBattleSessionProvider
__all__ = ('BattleSessionSetup', 'getBattleSessionConfig')

def getBattleSessionConfig(manager):
    """ Configures services for package battle_control.
    :param manager: helpers.dependency.DependencyManager
    """
    manager.bindInstance(IBattleSessionProvider, BattleSessionProvider(), finalizer='stop')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\battle_control\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:47:38 St�edn� Evropa (b�n� �as)
