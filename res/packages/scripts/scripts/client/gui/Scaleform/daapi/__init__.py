# 2017.02.03 21:48:57 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/__init__.py
from gui.Scaleform.framework.entities.View import View

class LobbySubView(View):
    __background_alpha__ = 0.6

    def setEnvironment(self, app):
        app.setBackgroundAlpha(self.__background_alpha__)
        super(LobbySubView, self).setEnvironment(app)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:57 St�edn� Evropa (b�n� �as)
