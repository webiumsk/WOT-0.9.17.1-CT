# 2017.02.03 21:50:11 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/inputChecker/__init__.py
from gui.Scaleform.daapi.view.lobby.inputChecker.InputChecker import InputChecker
from gui.Scaleform.framework import ViewTypes, ScopeTemplates, ViewSettings

class INPUT_CHECKER_ALIASES(object):
    INPUT_CHECKER = 'inputCheckerComponent'


def getContextMenuHandlers():
    return ()


def getViewSettings():
    return (ViewSettings(INPUT_CHECKER_ALIASES.INPUT_CHECKER, InputChecker, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),)


def getBusinessHandlers():
    return ()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\inputChecker\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:11 St�edn� Evropa (b�n� �as)
