# 2017.02.03 21:51:02 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PremiumWindowMeta.py
from gui.Scaleform.daapi.view.meta.SimpleWindowMeta import SimpleWindowMeta

class PremiumWindowMeta(SimpleWindowMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleWindowMeta
    """

    def onRateClick(self, rateId):
        self._printOverrideError('onRateClick')

    def as_setHeaderS(self, prc, bonus1, bonus2):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeader(prc, bonus1, bonus2)

    def as_setRatesS(self, data):
        """
        :param data: Represented by PremiumWindowRatesVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setRates(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\PremiumWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:51:02 St�edn� Evropa (b�n� �as)
