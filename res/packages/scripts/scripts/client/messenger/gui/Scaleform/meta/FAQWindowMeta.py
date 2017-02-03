# 2017.02.03 21:53:32 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/FAQWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FAQWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onLinkClicked(self, name):
        self._printOverrideError('onLinkClicked')

    def as_appendTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_appendText(text)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\messenger\gui\Scaleform\meta\FAQWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:53:32 Støední Evropa (bìžný èas)
