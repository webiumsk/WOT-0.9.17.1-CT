# 2017.02.03 21:58:51 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/idlelib/dynOptionMenuWidget.py
"""
OptionMenu widget modified to allow dynamic menu reconfiguration
and setting of highlightthickness
"""
from Tkinter import OptionMenu
from Tkinter import _setit
import copy

class DynOptionMenu(OptionMenu):
    """
    unlike OptionMenu, our kwargs can include highlightthickness
    """

    def __init__(self, master, variable, value, *values, **kwargs):
        kwargsCopy = copy.copy(kwargs)
        if 'highlightthickness' in kwargs.keys():
            del kwargs['highlightthickness']
        OptionMenu.__init__(self, master, variable, value, *values, **kwargs)
        self.config(highlightthickness=kwargsCopy.get('highlightthickness'))
        self.variable = variable
        self.command = kwargs.get('command')

    def SetMenu(self, valueList, value = None):
        """
        clear and reload the menu with a new set of options.
        valueList - list of new options
        value - initial value to set the optionmenu's menubutton to
        """
        self['menu'].delete(0, 'end')
        for item in valueList:
            self['menu'].add_command(label=item, command=_setit(self.variable, item, self.command))

        if value:
            self.variable.set(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\Lib\idlelib\dynOptionMenuWidget.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:58:51 St�edn� Evropa (b�n� �as)
