# 2017.02.03 21:53:24 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/messenger/gui/__init__.py
from messenger.m_constants import MESSENGER_SCOPE

def setGUIEntries(decorator):
    from messenger.gui.Scaleform.battle_entry import BattleEntry
    from messenger.gui.Scaleform.lobby_entry import LobbyEntry
    decorator.setEntry(MESSENGER_SCOPE.LOBBY, LobbyEntry())
    decorator.setEntry(MESSENGER_SCOPE.BATTLE, BattleEntry())
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\messenger\gui\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:53:24 St�edn� Evropa (b�n� �as)
