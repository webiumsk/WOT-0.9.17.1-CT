# 2017.02.03 21:52:14 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/fortifications/FortFinder.py
import BigWorld
from gui.shared.utils.requesters import DataRequestsByIDProcessor, DataRequestCtx

class FortFinder(DataRequestsByIDProcessor):

    def getSender(self):
        return BigWorld.player()

    def request(self, filterType, abbrevPattern, homePeripheryID, limit, lvlFrom, lvlTo, ownStartDefHourFrom, ownStartDefHourTo, nextOwnStartDefHourFrom, nextOwnStartDefHourTo, defHourChangeDay, extStartDefHourFrom, extStartDefHourTo, attackDay, ownFortLvl, ownProfitFactor10, avgBuildingLevel10, ownBattleCountForFort, firstDefaultQuery, electedClanDBIDs, callback = None):
        return self.doRequestEx(DataRequestCtx(), callback, 'requestFortPublicInfo', filterType, abbrevPattern, homePeripheryID, limit, lvlFrom, lvlTo, ownStartDefHourFrom, ownStartDefHourTo, nextOwnStartDefHourFrom, nextOwnStartDefHourTo, defHourChangeDay, extStartDefHourFrom, extStartDefHourTo, attackDay, ownFortLvl, ownProfitFactor10, avgBuildingLevel10, ownBattleCountForFort, firstDefaultQuery, electedClanDBIDs)

    def response(self, requestID, result, data):
        self._onResponseReceived(requestID, result, data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\shared\fortifications\FortFinder.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:52:14 St�edn� Evropa (b�n� �as)
