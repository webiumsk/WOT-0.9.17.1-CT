# 2017.02.03 21:49:39 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/__init__.py
from gui.shared.utils.functions import getArenaGeomentryName
from helpers.i18n import makeString
MAX_MEMBERS_IN_CLAN = 100

def getI18ArenaById(arenaId):
    return makeString('#arenas:%s/name' % getArenaGeomentryName(arenaId))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\clans\profile\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:49:39 St�edn� Evropa (b�n� �as)
