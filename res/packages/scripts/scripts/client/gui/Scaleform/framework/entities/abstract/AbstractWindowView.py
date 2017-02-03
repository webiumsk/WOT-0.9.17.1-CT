# 2017.02.03 21:51:14 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/AbstractWindowView.py
from gui.Scaleform.daapi.view.meta.WindowViewMeta import WindowViewMeta

class AbstractWindowView(WindowViewMeta):

    def __init__(self, ctx = None):
        super(AbstractWindowView, self).__init__()

    def _populate(self):
        super(AbstractWindowView, self)._populate()

    def onTryClosing(self):
        return True
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\AbstractWindowView.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:51:14 Støední Evropa (bìžný èas)
