# 2017.02.03 21:48:21 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/miniclient/promo_controller.py
from helpers import aop

class ShowPromoBrowserPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.game_control.PromoController', 'PromoController', 'onLobbyInited', aspects=(aop.DummyAspect,))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\miniclient\promo_controller.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:21 Støední Evropa (bìžný èas)
