# 2017.02.03 21:47:45 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/battle_control/controllers/interfaces.py


class IBattleController(object):
    __slots__ = ()

    def startControl(self, *args):
        raise NotImplementedError

    def stopControl(self):
        raise NotImplementedError

    def getControllerID(self):
        raise NotImplementedError


class IBattleControllersRepository(object):
    __slots__ = ()

    @classmethod
    def create(cls, setup):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError

    def getController(self, ctrlID):
        raise NotImplementedError

    def addController(self, ctrl):
        raise NotImplementedError
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\battle_control\controllers\interfaces.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:47:45 St�edn� Evropa (b�n� �as)
