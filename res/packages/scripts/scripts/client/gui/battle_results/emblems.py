# 2017.02.03 21:47:51 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/battle_results/emblems.py
from adisp import process
from gui.battle_results.settings import EMBLEM_TYPE
from gui.shared.ClanCache import g_clanCache

class EmblemFetcher(object):
    __slots__ = ('_formationDBID', '_url', '_callback')

    def __init__(self, formationDBID):
        super(EmblemFetcher, self).__init__()
        self._formationDBID = formationDBID
        self._url = ''
        self._callback = None
        return

    def clear(self):
        self._callback = None
        return

    def fetch(self, callback):
        callback(None)
        return

    def getURL(self):
        return self._url


class ClanEmblemFetcher(EmblemFetcher):
    __slots__ = ('_url',)

    def __init__(self, formationDBID, textureID):
        super(ClanEmblemFetcher, self).__init__(formationDBID)
        self._url = textureID

    @process
    def fetch(self, callback):
        self._url = yield g_clanCache.getClanEmblemTextureID(self._formationDBID, False, self._url)
        callback(self._url)


def createFetcher(ctx):
    emblemType = ctx.getEmblemType()
    fetcher = None
    if emblemType == EMBLEM_TYPE.CLAN:
        fetcher = ClanEmblemFetcher(ctx.getFormationDBID(), ctx.getTextureID())
    return fetcher
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\battle_results\emblems.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:47:51 St�edn� Evropa (b�n� �as)
