# 2017.02.03 21:53:33 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/messenger/gui/Scaleform/view/battle/__init__.py
from gui.Scaleform.framework import ViewTypes, ViewSettings, ScopeTemplates

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from messenger.gui.Scaleform.view.battle import messenger_view
    from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
    return (ViewSettings(BATTLE_VIEW_ALIASES.BATTLE_MESSENGER, messenger_view.BattleMessengerView, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),)


def getBusinessHandlers():
    return ()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\messenger\gui\Scaleform\view\battle\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:53:33 St�edn� Evropa (b�n� �as)
