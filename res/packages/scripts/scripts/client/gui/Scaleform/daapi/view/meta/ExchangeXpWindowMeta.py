# 2017.02.03 21:50:53 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ExchangeXpWindowMeta.py
from gui.Scaleform.daapi.view.lobby.exchange.BaseExchangeWindow import BaseExchangeWindow

class ExchangeXpWindowMeta(BaseExchangeWindow):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseExchangeWindow
    """

    def as_vehiclesDataChangedS(self, data):
        """
        :param data: Represented by ExchangeXPWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_vehiclesDataChanged(data)

    def as_totalExperienceChangedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_totalExperienceChanged(value)

    def as_setWalletStatusS(self, walletStatus):
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ExchangeXpWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:50:54 St�edn� Evropa (b�n� �as)
