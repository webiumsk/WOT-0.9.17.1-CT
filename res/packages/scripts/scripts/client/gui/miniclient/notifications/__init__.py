# 2017.02.03 21:48:24 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/miniclient/notifications/__init__.py
from gui.miniclient.notifications.clan_applications import ClanMultiNotifPointCut, ClanSingleInviteNotifPointCut, ClanSingleAppNotifPointCut, ClanSingleNotificationHtmlTextFormatterPointCut

def configure_pointcuts():
    ClanSingleAppNotifPointCut()
    ClanSingleInviteNotifPointCut()
    ClanMultiNotifPointCut()
    ClanSingleNotificationHtmlTextFormatterPointCut()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\miniclient\notifications\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:24 Støední Evropa (bìžný èas)
