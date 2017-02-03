# 2017.02.03 21:54:00 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/notification/AlertController.py
from gui import DialogsInterface
from gui.Scaleform.daapi.view.dialogs.SystemMessageMeta import SystemMessageMeta
from notification.BaseMessagesController import BaseMessagesController
import Event
from adisp import process

class AlertController(BaseMessagesController):

    def __init__(self, model):
        BaseMessagesController.__init__(self, model)
        self.__actualDisplayingAlerts = 0
        self.onAllAlertsClosed = Event.Event()

    @process
    def showAlertMessage(self, notification):
        self.__actualDisplayingAlerts += 1
        yield DialogsInterface.showDialog(SystemMessageMeta(notification))
        self.__actualDisplayingAlerts -= 1
        if self.__actualDisplayingAlerts == 0:
            self.onAllAlertsClosed()

    def isAlertShowing(self):
        return self.__actualDisplayingAlerts > 0
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\notification\AlertController.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:54:00 St�edn� Evropa (b�n� �as)
