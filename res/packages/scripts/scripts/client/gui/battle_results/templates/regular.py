# 2017.02.03 21:47:59 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/battle_results/templates/regular.py
from gui.Scaleform.genConsts.BATTLE_EFFICIENCY_TYPES import BATTLE_EFFICIENCY_TYPES
from gui.Scaleform.locale.BATTLE_RESULTS import BATTLE_RESULTS
from gui.Scaleform.locale.INGAME_GUI import INGAME_GUI
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.battle_results.components import base
from gui.battle_results.components import common
from gui.battle_results.components import details
from gui.battle_results.components import personal
from gui.battle_results.components import progress
from gui.battle_results.components import shared
from gui.battle_results.components import style
from gui.battle_results.components import vehicles
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from helpers import i18n
_REGULAR_TABS_VO_META = base.ListMeta([{'label': i18n.makeString(MENU.FINALSTATISTIC_TABS_COMMONSTATS),
  'linkage': 'CommonStats',
  'showWndBg': False}, {'label': i18n.makeString(MENU.FINALSTATISTIC_TABS_TEAMSTATS),
  'linkage': 'TeamStatsUI',
  'showWndBg': False}, {'label': i18n.makeString(MENU.FINALSTATISTIC_TABS_DETAILSSTATS),
  'linkage': 'DetailsStatsViewUI',
  'showWndBg': True}])
_MULTI_TEAM_TABS_VO_META = base.ListMeta([{'label': MENU.FINALSTATISTIC_TABS_COMMONSTATS,
  'linkage': 'CommonStats',
  'showWndBg': False}, {'label': MENU.FINALSTATISTIC_TABS_TEAMSTATS,
  'linkage': 'MultiteamStatsUI',
  'showWndBg': False}, {'label': MENU.FINALSTATISTIC_TABS_DETAILSSTATS,
  'linkage': 'DetailsStatsViewUI',
  'showWndBg': True}])
REGULAR_TABS_BLOCK = base.StatsBlock(_REGULAR_TABS_VO_META, 'tabInfo')
MULTI_TEAM_TABS_BLOCK = base.StatsBlock(_MULTI_TEAM_TABS_VO_META, 'tabInfo')
_TEXT_VO_META = base.DictMeta({'windowTitle': i18n.makeString(MENU.FINALSTATISTIC_WINDOW_TITLE),
 'shareButtonLabel': i18n.makeString(BATTLE_RESULTS.COMMON_RESULTSSHAREBTN),
 'shareButtonTooltip': i18n.makeString(TOOLTIPS.BATTLERESULTS_FORTRESOURCE_RESULTSSHAREBTN),
 'ownTitle': BATTLE_RESULTS.TEAM_STATS_OWNTEAM,
 'enemyTitle': BATTLE_RESULTS.TEAM_STATS_ENEMYTEAM})
REGULAR_TEXT_STATS_BLOCK = base.StatsBlock(_TEXT_VO_META, 'textData')
CLAN_TEXT_STATS_BLOCK = REGULAR_TEXT_STATS_BLOCK.clone()
CLAN_TEXT_STATS_BLOCK.addComponent(0, common.AllyTeamClanTitle('ownTitle'))
CLAN_TEXT_STATS_BLOCK.addComponent(1, common.EnemyTeamClanTitle('enemyTitle'))
_COMMON_VO_META = base.DictMeta({'iconType': 'tank',
 'sortDirection': 'descending',
 'wasInBattle': True,
 'arenaCreateTimeStr': '',
 'arenaStr': '',
 'arenaIcon': '',
 'duration': '',
 'bonusType': 0,
 'clans': [],
 'resultShortStr': '',
 'resultStr': '',
 'finishReasonStr': '',
 'playerNameStr': '',
 'playerFullNameStr': '',
 'clanNameStr': '',
 'regionNameStr': '',
 'playerVehicles': [],
 'playerVehicleNames': [],
 'falloutMode': '',
 'overtime': {},
 'totalFortResourceStr': '',
 'totalInfluenceStr': '',
 'timeStats': [],
 'clientArenaIdx': 0,
 'uiVisibility': 0})
_CLAN_COMMON_VO_META = base.PropertyMeta((('clanDBID', -1, 'clanDBID'), ('clanAbbrev', '', 'clanAbbrev')))
_CLAN_COMMON_VO_META.bind(common.ClanInfoBlock)
CLANS_COMMON_VO_META = base.PropertyMeta((('allies', common.ClanInfoBlock(field='allies'), 'allies'), ('enemies', common.ClanInfoBlock(field='enemies'), 'enemies')))
CLANS_COMMON_VO_META.bind(common.ClansInfoBlock)
_PERSONAL_VEHICLE_VO_META = base.PropertyMeta((('isPrematureLeave', False, 'isPrematureLeave'),
 ('flag', '', 'nationName'),
 ('tankIcon', '../maps/icons/vehicle/noImage.png', 'vehicleIcon'),
 ('killerID', 0, 'killerID'),
 ('vehicleStateStr', '', 'vehicleState'),
 ('vehicleStatePrefixStr', '', 'vehicleStatePrefix'),
 ('vehicleStateSuffixStr', '', 'vehicleStateSuffix')))
_PERSONAL_VEHICLE_VO_META.bind(personal.PersonalVehicleBlock)
_PERSONAL_PLAYER_NAME_VO_META = base.PropertyMeta((('playerNameStr', '', 'nameLabel'),
 ('playerFullNameStr', '', 'fullNameLabel'),
 ('clanNameStr', '', 'clanLabel'),
 ('regionNameStr', '', 'regionLabel')))
_PERSONAL_PLAYER_NAME_VO_META.bind(personal.PersonalPlayerNameBlock)
_PERSONAL_PLAYER_NAME_VO_META.bind(personal.DetailsPlayerNameBlock)
_KILLER_NAME_VO_META = base.PropertyMeta((('killerNameStr', '', 'nameLabel'),
 ('killerFullNameStr', '', 'fullNameLabel'),
 ('killerClanNameStr', '', 'clanLabel'),
 ('killerRegionNameStr', '', 'regionLabel')))
_KILLER_NAME_VO_META.bind(personal.KillerPlayerNameBlock)
_TIME_STATS_BLOCK = base.StatsBlock(base.ListMeta(runtime=False), 'timeStats', _RECORD.COMMON)
_TIME_STATS_BLOCK.addComponent(0, common.ArenaShortTimeVO('arenaCreateTimeOnlyStr', 'arenaCreateTime'))
_TIME_STATS_BLOCK.addComponent(1, common.ArenaDurationVO('duration', 'duration'))
_TIME_STATS_BLOCK.addComponent(2, common.PlayerKillingTimeVO('playerKilled'))
_STATS_SORTING_VO_META = base.PropertyMeta((('iconType', 'tank', 'criteria'), ('sortDirection', 'descending', 'direction')))
_STATS_SORTING_VO_META.bind(shared.SortingBlock)
FINISH_RESULT_VO_META = base.PropertyMeta((('finishReasonStr', '', 'finishReasonLabel'), ('resultShortStr', '', 'shortResultLabel'), ('resultStr', '', 'fullResultLabel')))
FINISH_RESULT_VO_META.bind(common.RegularFinishResultBlock)
REGULAR_COMMON_STATS_BLOCK = base.StatsBlock(_COMMON_VO_META, 'common')
REGULAR_COMMON_STATS_BLOCK.addComponent(0, shared.RegularSortingBlock())
REGULAR_COMMON_STATS_BLOCK.addComponent(1, shared.WasInBattleItem('wasInBattle'))
REGULAR_COMMON_STATS_BLOCK.addComponent(2, common.ArenaDateTimeItem('arenaCreateTimeStr', _RECORD.COMMON, 'arenaCreateTime'))
REGULAR_COMMON_STATS_BLOCK.addComponent(3, common.RegularArenaFullNameItem('arenaStr'))
REGULAR_COMMON_STATS_BLOCK.addComponent(4, common.ArenaIconItem('arenaIcon', _RECORD.COMMON))
REGULAR_COMMON_STATS_BLOCK.addComponent(5, common.ArenaDurationItem('duration', _RECORD.COMMON, 'duration'))
REGULAR_COMMON_STATS_BLOCK.addComponent(6, base.StatsItem('bonusType', _RECORD.COMMON, 'bonusType'))
REGULAR_COMMON_STATS_BLOCK.addComponent(7, common.RegularFinishResultBlock())
REGULAR_COMMON_STATS_BLOCK.addComponent(8, personal.PersonalPlayerNameBlock())
REGULAR_COMMON_STATS_BLOCK.addComponent(9, personal.PersonalVehicleNamesBlock(base.ListMeta(), 'playerVehicleNames'))
REGULAR_COMMON_STATS_BLOCK.addComponent(10, personal.PersonalVehiclesBlock(base.ListMeta(), 'playerVehicles', _RECORD.PERSONAL))
REGULAR_COMMON_STATS_BLOCK.addComponent(11, _TIME_STATS_BLOCK.clone())
REGULAR_COMMON_STATS_BLOCK.addComponent(12, shared.ClientIndexItem('clientArenaIdx'))
REGULAR_COMMON_STATS_BLOCK.addComponent(13, common.TeamsUiVisibility('uiVisibility'))
_PERSONAL_VO_META = base.DictMeta({'isPremium': False,
 'hasGetPremBtn': False,
 'getPremVO': {},
 'isLegionnaire': False,
 'creditsStr': '0',
 'xpStr': '0',
 'fortResourceTotal': '',
 'efficiencyHeader': {},
 'details': [],
 'creditsNoPremValues': [],
 'creditsPremValues': [],
 'creditsData': [],
 'xpTitleStrings': [],
 'xpNoPremValues': [],
 'xpPremValues': [],
 'xpData': [],
 'resValues': [],
 'resPremValues': [],
 'resourceData': [],
 'statValues': [],
 'achievementsLeft': [],
 'achievementsRight': [],
 'showNoIncomeAlert': False,
 'noIncomeAlert': None})
_PREMIUM_BUY_VO_META = base.PropertyMeta((('arenaUniqueID', 0, 'clientIndex'), ('creditsDiff', 0, 'creditsDiff'), ('xpDiff', 0, 'xpDiff')))
_PREMIUM_BUY_VO_META.bind(personal.PremiumBuyBlock)
_DAMAGE_DETAILS_VO_META = base.PropertyMeta((('damageTotalItems', 0, 'piercings'), ('damageDealtVals', None, 'damageDealtValues'), ('damageDealtNames', None, 'damageDealtNames')))
_DAMAGE_DETAILS_VO_META.bind(personal.DamageDetailsBlock)
_ARMOR_USING_DETAILS_VO_META = base.PropertyMeta((('armorTotalItems', 0, 'usedArmorCount'), ('armorVals', None, 'armorValues'), ('armorNames', None, 'armorNames')))
_ARMOR_USING_DETAILS_VO_META.bind(personal.ArmorUsingDetailsBlock)
_ASSIST_USING_DETAILS_VO_META = base.PropertyMeta((('damageAssisted', 0, 'damageAssisted'), ('damageAssistedVals', None, 'damageAssistedValues'), ('damageAssistedNames', None, 'damageAssistedNames')))
_ASSIST_USING_DETAILS_VO_META.bind(personal.AssistDetailsBlock)
_CRITS_DETAILS_VO_META = base.PropertyMeta((('critsCount', 0, 'critsCount'),
 ('criticalDevices', [], 'criticalDevices'),
 ('destroyedDevices', [], 'destroyedDevices'),
 ('destroyedTankmen', [], 'destroyedTankmen')))
_CRITS_DETAILS_VO_META.bind(personal.CritsDetailsBlock)
_TEAM_BASES_VO_META = base.PropertyMeta((('baseLabel', '', 'label'),
 ('captureTotalItems', 0, 'captureTotalItems'),
 ('defenceTotalItems', 0, 'defenceTotalItems'),
 ('captureVals', None, 'captureValues'),
 ('captureNames', None, 'captureNames'),
 ('defenceVals', None, 'defenceValues'),
 ('defenceNames', None, 'defenceNames')))
_TEAM_BASES_VO_META.bind(personal.TeamBaseDetailsBlock)
_TEAM_BASES_VO_META.bind(personal.DominationTeamBaseDetailBlock)
_TEAM_BASES_VO_META.bind(personal.AllyTeamBaseDetailBlock)
_TEAM_BASES_VO_META.bind(personal.EnemyTeamBaseDetailBlock)
_DETAILS_PLAYER_NAME_VO_META = base.PropertyMeta((('playerName', '', 'nameLabel'),
 ('playerFullName', '', 'fullNameLabel'),
 ('playerClan', '', 'clanLabel'),
 ('playerRegion', '', 'regionLabel')))
_DETAILS_PLAYER_NAME_VO_META.bind(personal.DetailsPlayerNameBlock)
_EFFICIENCY_DETAILS_VO_META = base.PropertyMeta((('deathReason', -1, 'deathReason'),
 ('spotted', 0, 'spotted'),
 ('piercings', 0, 'piercings'),
 ('damageDealt', 0, 'damageDealt'),
 ('killCount', 0, 'killCount'),
 ('tankIcon', '../maps/icons/vehicle/small/noImage.png', 'vehicleIcon'),
 ('vehicleName', i18n.makeString(INGAME_GUI.PLAYERS_PANEL_UNKNOWN_VEHICLE), 'vehicleName')))
_EFFICIENCY_DETAILS_VO_META.bind(personal.EnemyDetailsBlock)
_ACHIEVEMENT_ICON_VO_META = base.PropertyMeta((('big', '', 'big'), ('small', '', 'small')))
_ACHIEVEMENT_ICON_VO_META.bind(shared.AchievementIcon)
_ACHIEVEMENT_VO_META = base.PropertyMeta((('type', '', 'type'),
 ('block', '', 'block'),
 ('inactive', False, 'inactive'),
 ('icon', shared.AchievementIcon(field='icon'), 'icon'),
 ('rank', None, 'rank'),
 ('localizedValue', None, 'i18nValue'),
 ('unic', False, 'isUnique'),
 ('isRare', False, 'isRare'),
 ('title', '', 'title'),
 ('description', '', 'description'),
 ('rareIconId', None, 'rareIconID'),
 ('isEpic', False, 'hasRibbon'),
 ('specialIcon', None, 'specialIcon'),
 ('customData', [], 'customData')))
_ACHIEVEMENT_VO_META.bind(shared.AchievementBlock)
_ACHIEVEMENTS_LIST_VO_META = base.DictMeta({'achievementsLeft': [],
 'achievementsRight': []})
_PERSONAL_ACHIEVEMENTS_BLOCK = personal.TotalPersonalAchievementsBlock(_ACHIEVEMENTS_LIST_VO_META.clone(), '', _RECORD.PERSONAL)
_PERSONAL_ACHIEVEMENTS_BLOCK.addNextComponent(shared.AchievementsBlock(base.ListMeta(), 'achievementsLeft'))
_PERSONAL_ACHIEVEMENTS_BLOCK.addNextComponent(shared.AchievementsBlock(base.ListMeta(), 'achievementsRight'))
_TOTAL_EFFICIENCY_HEADER_META = base.PropertyMeta(((BATTLE_EFFICIENCY_TYPES.DESTRUCTION, '-', 'kills'),
 (BATTLE_EFFICIENCY_TYPES.DAMAGE, '-', 'damageDealt'),
 (BATTLE_EFFICIENCY_TYPES.CRITS, '-', 'criticalDamages'),
 (BATTLE_EFFICIENCY_TYPES.ARMOR, '-', 'damageBlockedByArmor'),
 (BATTLE_EFFICIENCY_TYPES.ASSIST, '-', 'damageAssisted'),
 (BATTLE_EFFICIENCY_TYPES.DETECTION, '-', 'spotted'),
 ('killTooltip', None, 'killsTooltip'),
 ('damageTooltip', None, 'damageDealtTooltip'),
 ('critsTooltip', None, 'criticalDamagesTooltip'),
 ('armorTooltip', None, 'damageBlockedTooltip'),
 ('assistTooltip', None, 'damageAssistedTooltip'),
 ('spottedTooltip', None, 'spottedTooltip')))
_TOTAL_EFFICIENCY_HEADER_META.bind(personal.TotalEfficiencyDetailsHeader)
REGULAR_PERSONAL_STATS_BLOCK = base.StatsBlock(_PERSONAL_VO_META, 'personal')
REGULAR_PERSONAL_STATS_BLOCK.addComponent(0, personal.TotalEfficiencyDetailsHeader(_TOTAL_EFFICIENCY_HEADER_META, 'efficiencyHeader', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(1, personal.TotalEfficiencyDetailsBlock(base.ListMeta(), 'details', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(2, _PERSONAL_ACHIEVEMENTS_BLOCK)
REGULAR_PERSONAL_STATS_BLOCK.addComponent(3, personal.PremiumAccountFlag('isPremium'))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(4, personal.CanUpgradeToPremiumFlag('hasGetPremBtn'))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(5, personal.PremiumBuyBlock(field='getPremVO'))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(6, details.GainCreditsInBattleItem('creditsStr'))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(7, details.GainXPInBattleItem('xpStr'))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(8, details.BaseCreditsBlock(base.ListMeta(), 'creditsNoPremValues', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(9, details.PremiumCreditsBlock(base.ListMeta(), 'creditsPremValues', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(10, details.TotalMoneyDetailsBlock(base.ListMeta(), 'creditsData', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(11, details.XPTitleBlock(base.ListMeta(), 'xpTitleStrings', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(12, details.BaseXPBlock(base.ListMeta(), 'xpNoPremValues', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(13, details.PremiumXPBlock(base.ListMeta(), 'xpPremValues', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(14, details.TotalXPDetailsBlock(base.ListMeta(), 'xpData', _RECORD.PERSONAL))
REGULAR_PERSONAL_STATS_BLOCK.addComponent(15, vehicles.PersonalVehiclesRegularStatsBlock(base.ListMeta(), 'statValues', _RECORD.PERSONAL))
_TEAM_PLAYER_VO_META = base.PropertyMeta((('userName', '', 'nameLabel'),
 ('fullName', '', 'fullNameLabel'),
 ('clanAbbrev', '', 'clanLabel'),
 ('region', '', 'regionLabel'),
 ('igrType', 0, 'igrType')))
_TEAM_PLAYER_VO_META.bind(vehicles.TeamPlayerNameBlock)
VEHICLE_STATS_BLOCK_VO_META = base.PropertyMeta((('shots', 0, 'shots'),
 ('hits', style.SlashedValuesBlock('hits'), 'hits'),
 ('explosionHits', 0, 'explosionHits'),
 ('damageDealt', 0, 'damageDealt'),
 ('sniperDamageDealt', 0, 'sniperDamageDealt'),
 ('directHitsReceived', 0, 'directHitsReceived'),
 ('piercingsReceived', 0, 'piercingsReceived'),
 ('noDamageDirectHitsReceived', 0, 'noDamageDirectHitsReceived'),
 ('explosionHitsReceived', 0, 'explosionHitsReceived'),
 ('damageBlockedByArmor', 0, 'damageBlockedByArmor'),
 ('teamHitsDamage', style.RedSlashedValuesBlock('teamHitsDamage'), 'teamHitsDamage'),
 ('spotted', 0, 'spotted'),
 ('damagedKilled', style.SlashedValuesBlock('damagedKilled'), 'damagedKilled'),
 ('damageAssisted', 0, 'damageAssisted'),
 ('capturePointsVal', style.SlashedValuesBlock('capturePointsVal'), 'capturePoints'),
 ('mileage', style.MetersToKillometersItem('mileage'), 'mileage')))
VEHICLE_STATS_BLOCK_VO_META.bind(vehicles.RegularVehicleStatValuesBlock)
TEAM_ITEM_VO_META = base.PropertyMeta((('achievements', shared.AchievementsBlock(base.ListMeta(), 'achievements'), 'achievements'),
 ('medalsCount', 0, 'achievementsCount'),
 ('vehicleStateStr', '', 'vehicleState'),
 ('vehicleStatePrefixStr', '', 'vehicleStatePrefix'),
 ('vehicleStateSuffixStr', '', 'vehicleStateSuffix'),
 ('killerID', 0, 'killerID'),
 ('deathReason', -1, 'deathReason'),
 ('isPrematureLeave', False, 'isPrematureLeave'),
 ('vehicleCD', 0, 'intCD'),
 ('vehicleFullName', '', 'vehicleName'),
 ('tankIcon', '', 'vehicleIcon'),
 ('vehicleName', '', 'vehicleShortName'),
 ('vehicles', [], 'vehicles'),
 ('vehicleSort', '', 'vehicleSort'),
 ('xpSort', 0, 'xpSort'),
 ('isSelf', False, 'isPersonal'),
 ('kills', 0, 'kills'),
 ('tkills', 0, 'tkills'),
 ('realKills', 0, 'realKills'),
 ('xp', 0, 'xp'),
 ('damageDealt', 0, 'damageDealt'),
 ('playerId', 0, 'playerID'),
 ('userVO', vehicles.TeamPlayerNameBlock(field='userVO'), 'player'),
 ('squadID', 0, 'squadIndex'),
 ('isOwnSquad', False, 'isPersonalSquad'),
 ('statValues', vehicles.AllRegularVehicleStatValuesBlock(base.ListMeta(), 'statValues'), 'statValues'),
 ('resourceCount', 0, 'fortResource')))
TEAM_ITEM_VO_META.bind(vehicles.RegularVehicleStatsBlock)
TEAMS_VO_META = base.DictMeta({'team1': [],
 'team2': []})
REGULAR_TEAMS_STATS_BLOCK = vehicles.TwoTeamsStatsBlock(TEAMS_VO_META.clone(), '', _RECORD.VEHICLES)
REGULAR_TEAMS_STATS_BLOCK.addNextComponent(vehicles.RegularTeamStatsBlock(meta=base.ListMeta(), field='team1'))
REGULAR_TEAMS_STATS_BLOCK.addNextComponent(vehicles.RegularTeamStatsBlock(meta=base.ListMeta(), field='team2'))
VEHICLE_PROGRESS_STATS_BLOCK = progress.VehicleProgressBlock(base.ListMeta(), 'unlocks', _RECORD.PERSONAL)
QUESTS_PROGRESS_STATS_BLOCK = progress.QuestsProgressBlock(base.ListMeta(), 'quests', _RECORD.PERSONAL)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\battle_results\templates\regular.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:47:59 St�edn� Evropa (b�n� �as)
