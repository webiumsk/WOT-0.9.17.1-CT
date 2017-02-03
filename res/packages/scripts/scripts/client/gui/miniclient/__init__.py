# 2017.02.03 21:48:21 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/miniclient/__init__.py
import ResMgr
import contacts as _contacts
import continue_download as _continue_download
import dynamic_squads as _dynamic_squads
import event as _event
import fallout_controller as _fallout_controller
import preview as _preview
import promo_controller as _promo_controller
import shop as _shop
from constants import CONTENT_TYPE
from fortified_regions import configure_pointcuts as _configure_fort_pointcuts
from gui.miniclient.notifications import configure_pointcuts as _notifications_configure_pointcuts
from invitations import configure_pointcuts as _configure_invitation_pointcuts
from lobby import configure_pointcuts as _configure_lobby_pointcuts
from login import configure_pointcuts as _configure_login_pointcuts
from personal_quests import configure_pointcuts as _configure_personal_quests_pointcuts
from tech_tree import configure_pointcuts as _configure_tech_tree_pointcuts
from vehicle_compare import configure_pointcuts as _configure_vehicle_compare_pointcuts

def configure_state():
    content_type = ResMgr.activeContentType()
    if content_type == CONTENT_TYPE.SANDBOX:
        config = _get_config(content_type)
        _shop.OnShopItemWrapPointcut(config)
        _continue_download.OnHyperlinkClickPointcut()
        _continue_download.OnSquadHyperlinkClickPointcut()
        _continue_download.PrepareLibrariesListPointcut()
        _continue_download.OnBrowserHyperlinkClickPointcut()
        _continue_download.OnFailLoadingFramePointcut()
        _contacts.CreateSquadPointcut()
        _configure_lobby_pointcuts(config)
        _configure_login_pointcuts()
        _notifications_configure_pointcuts()
        _configure_fort_pointcuts()
        _configure_tech_tree_pointcuts(config)
        _configure_invitation_pointcuts()
        _configure_personal_quests_pointcuts()
        _dynamic_squads.ParametrizeInitPointcut()
        _dynamic_squads.DisableGameSettingPointcut()
        _dynamic_squads.InviteReceivedMessagePointcut()
        _promo_controller.ShowPromoBrowserPointcut()
        _fallout_controller.InitFalloutPointcut()
        _event.InitEventPointcut()
        _preview.ChangeVehicleIsPreviewAllowed(config)
        _configure_vehicle_compare_pointcuts()


def _get_config(content_type):

    def vehicle_filter(vehicle_item):
        extraCondition = not vehicle_item.isOnlyForEventBattles
        if content_type == CONTENT_TYPE.SANDBOX:
            max_vehicle_level = 2
            extraCondition = extraCondition and not vehicle_item.isExcludedFromSandbox
        elif content_type == CONTENT_TYPE.TUTORIAL:
            max_vehicle_level = 1
        else:
            max_vehicle_level = 10
            extraCondition = True
        return vehicle_item.level <= max_vehicle_level and extraCondition

    return {'vehicle_is_available': vehicle_filter}


__all__ = ('configure_state',)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\miniclient\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:21 St�edn� Evropa (b�n� �as)
