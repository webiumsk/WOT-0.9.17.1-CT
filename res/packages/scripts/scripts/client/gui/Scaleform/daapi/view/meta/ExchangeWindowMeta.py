# 2017.02.03 21:50:53 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ExchangeWindowMeta.py
from gui.Scaleform.daapi.view.lobby.exchange.BaseExchangeWindow import BaseExchangeWindow

class ExchangeWindowMeta(BaseExchangeWindow):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseExchangeWindow
    """

    def as_setSecondaryCurrencyS(self, credits):
        if self._isDAAPIInited():
            return self.flashObject.as_setSecondaryCurrency(credits)

    def as_setWalletStatusS(self, walletStatus):
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ExchangeWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:53 St�edn� Evropa (b�n� �as)
