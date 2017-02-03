# 2017.02.03 21:51:14 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/EventSystemEntity.py
from gui.Scaleform.framework.entities.DisposableEntity import DisposableEntity
from gui.shared import g_eventBus, EVENT_BUS_SCOPE

class EventSystemEntity(DisposableEntity):

    def fireEvent(self, event, scope = EVENT_BUS_SCOPE.DEFAULT):
        g_eventBus.handleEvent(event, scope=scope)

    def addListener(self, eventType, handler, scope = EVENT_BUS_SCOPE.DEFAULT):
        g_eventBus.addListener(eventType, handler, scope=scope)

    def removeListener(self, eventType, handler, scope = EVENT_BUS_SCOPE.DEFAULT):
        g_eventBus.removeListener(eventType, handler, scope)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\EventSystemEntity.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:51:14 St�edn� Evropa (b�n� �as)
