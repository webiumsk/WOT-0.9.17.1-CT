# 2017.02.03 21:51:16 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/framework/managers/CacheManager.py
from gui import GUI_SETTINGS
from gui.Scaleform.framework.entities.abstract.CacheManagerMeta import CacheManagerMeta

class CacheManager(CacheManagerMeta):

    def __init__(self):
        super(CacheManager, self).__init__()
        self.__settings = GUI_SETTINGS.cache

    def getSettings(self):
        return self.__settings
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\managers\CacheManager.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:51:16 St�edn� Evropa (b�n� �as)
