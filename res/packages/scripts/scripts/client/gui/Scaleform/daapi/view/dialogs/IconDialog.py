# 2017.02.03 21:49:22 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/IconDialog.py
from gui.Scaleform.daapi.view.meta.IconDialogMeta import IconDialogMeta

class IconDialog(IconDialogMeta):

    def __init__(self, meta, handler):
        super(IconDialog, self).__init__(meta.getMessage(), meta.getTitle(), meta.getButtonLabels(), meta.getCallbackWrapper(handler))
        self._meta = meta

    def _populate(self):
        super(IconDialog, self)._populate()
        self.as_setIconS(self._meta.getIcon())

    def _dispose(self):
        self._meta = None
        super(IconDialog, self)._dispose()
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\dialogs\IconDialog.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:49:22 Støední Evropa (bìžný èas)
