# 2017.02.03 22:00:26 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-mac/MiniAEFrame.py
"""MiniAEFrame - A minimal AppleEvent Application framework.

There are two classes:
    AEServer -- a mixin class offering nice AE handling.
    MiniApplication -- a very minimal alternative to FrameWork.py,
        only suitable for the simplest of AppleEvent servers.
"""
from warnings import warnpy3k
warnpy3k('In 3.x, the MiniAEFrame module is removed.', stacklevel=2)
import traceback
import MacOS
from Carbon import AE
from Carbon.AppleEvents import *
from Carbon import Evt
from Carbon.Events import *
from Carbon import Menu
from Carbon import Win
from Carbon.Windows import *
from Carbon import Qd
import aetools
import EasyDialogs
kHighLevelEvent = 23

class MiniApplication:
    """A minimal FrameWork.Application-like class"""

    def __init__(self):
        self.quitting = 0
        self.appleid = 1
        self.quitid = 2
        Menu.ClearMenuBar()
        self.applemenu = applemenu = Menu.NewMenu(self.appleid, '\x14')
        applemenu.AppendMenu('%s;(-' % self.getaboutmenutext())
        if MacOS.runtimemodel == 'ppc':
            applemenu.AppendResMenu('DRVR')
        applemenu.InsertMenu(0)
        self.quitmenu = Menu.NewMenu(self.quitid, 'File')
        self.quitmenu.AppendMenu('Quit')
        self.quitmenu.SetItemCmd(1, ord('Q'))
        self.quitmenu.InsertMenu(0)
        Menu.DrawMenuBar()

    def __del__(self):
        self.close()

    def close(self):
        pass

    def mainloop(self, mask = everyEvent, timeout = 3600):
        while not self.quitting:
            self.dooneevent(mask, timeout)

    def _quit(self):
        self.quitting = 1

    def dooneevent(self, mask = everyEvent, timeout = 3600):
        got, event = Evt.WaitNextEvent(mask, timeout)
        if got:
            self.lowlevelhandler(event)

    def lowlevelhandler(self, event):
        what, message, when, where, modifiers = event
        h, v = where
        if what == kHighLevelEvent:
            msg = 'High Level Event: %r %r' % (code(message), code(h | v << 16))
            try:
                AE.AEProcessAppleEvent(event)
            except AE.Error as err:
                print 'AE error: ', err
                print 'in', msg
                traceback.print_exc()

            return
        if what == keyDown:
            c = chr(message & charCodeMask)
            if modifiers & cmdKey:
                if c == '.':
                    raise KeyboardInterrupt, 'Command-period'
                if c == 'q':
                    if hasattr(MacOS, 'OutputSeen'):
                        MacOS.OutputSeen()
                    self.quitting = 1
                    return
        elif what == mouseDown:
            partcode, window = Win.FindWindow(where)
            if partcode == inMenuBar:
                result = Menu.MenuSelect(where)
                id = result >> 16 & 65535
                item = result & 65535
                if id == self.appleid:
                    if item == 1:
                        EasyDialogs.Message(self.getabouttext())
                    elif item > 1 and hasattr(Menu, 'OpenDeskAcc'):
                        name = self.applemenu.GetMenuItemText(item)
                        Menu.OpenDeskAcc(name)
                elif id == self.quitid and item == 1:
                    if hasattr(MacOS, 'OutputSeen'):
                        MacOS.OutputSeen()
                    self.quitting = 1
                Menu.HiliteMenu(0)
                return
        if hasattr(MacOS, 'HandleEvent'):
            MacOS.HandleEvent(event)
        else:
            print 'Unhandled event:', event

    def getabouttext(self):
        return self.__class__.__name__

    def getaboutmenutext(self):
        return 'About %s\xc9' % self.__class__.__name__


class AEServer:

    def __init__(self):
        self.ae_handlers = {}

    def installaehandler(self, classe, type, callback):
        AE.AEInstallEventHandler(classe, type, self.callback_wrapper)
        self.ae_handlers[classe, type] = callback

    def close(self):
        for classe, type in self.ae_handlers.keys():
            AE.AERemoveEventHandler(classe, type)

    def callback_wrapper(self, _request, _reply):
        _parameters, _attributes = aetools.unpackevent(_request)
        _class = _attributes['evcl'].type
        _type = _attributes['evid'].type
        if (_class, _type) in self.ae_handlers:
            _function = self.ae_handlers[_class, _type]
        elif (_class, '****') in self.ae_handlers:
            _function = self.ae_handlers[_class, '****']
        elif ('****', '****') in self.ae_handlers:
            _function = self.ae_handlers[('****', '****')]
        else:
            raise 'Cannot happen: AE callback without handler', (_class, _type)
        _parameters['_attributes'] = _attributes
        _parameters['_class'] = _class
        _parameters['_type'] = _type
        if '----' in _parameters:
            _object = _parameters['----']
            del _parameters['----']
            rv = _function(_object, **_parameters)
        else:
            rv = _function(**_parameters)
        if rv is None:
            aetools.packevent(_reply, {})
        else:
            aetools.packevent(_reply, {'----': rv})
        return


def code(x):
    """Convert a long int to the 4-character code it really is"""
    s = ''
    for i in range(4):
        x, c = divmod(x, 256)
        s = chr(c) + s

    return s


class _Test(AEServer, MiniApplication):
    """Mini test application, handles required events"""

    def __init__(self):
        MiniApplication.__init__(self)
        AEServer.__init__(self)
        self.installaehandler('aevt', 'oapp', self.open_app)
        self.installaehandler('aevt', 'quit', self.quit)
        self.installaehandler('****', '****', self.other)
        self.mainloop()

    def quit(self, **args):
        self._quit()

    def open_app(self, **args):
        pass

    def other(self, _object = None, _class = None, _type = None, **args):
        print 'AppleEvent', (_class, _type), 'for', _object, 'Other args:', args


if __name__ == '__main__':
    _Test()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\Lib\plat-mac\MiniAEFrame.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 22:00:27 St�edn� Evropa (b�n� �as)