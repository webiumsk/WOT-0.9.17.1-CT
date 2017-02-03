# 2017.02.03 21:54:07 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/skeletons/gui/system_messages.py


class ISystemMessages(object):

    def init(self):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError

    def pushMessage(self, text, type, priority = None):
        raise NotImplementedError

    def pushI18nMessage(self, key, *args, **kwargs):
        raise NotImplementedError
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\skeletons\gui\system_messages.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:54:07 Støední Evropa (bìžný èas)
