# 2017.02.03 21:50:53 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/DestroyTimersPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class DestroyTimersPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_showS(self, timerTypeID, timerViewTypeID):
        if self._isDAAPIInited():
            return self.flashObject.as_show(timerTypeID, timerViewTypeID)

    def as_hideS(self, timerTypeID):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(timerTypeID)

    def as_setTimeInSecondsS(self, timerTypeID, totalSeconds, currentTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimeInSeconds(timerTypeID, totalSeconds, currentTime)

    def as_setTimeSnapshotS(self, timerTypeID, totalSeconds, timeLeft):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimeSnapshot(timerTypeID, totalSeconds, timeLeft)

    def as_setSpeedS(self, speed):
        if self._isDAAPIInited():
            return self.flashObject.as_setSpeed(speed)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\DestroyTimersPanelMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:53 St�edn� Evropa (b�n� �as)
