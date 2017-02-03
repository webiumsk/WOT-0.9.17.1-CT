# 2017.02.03 21:47:02 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/AvatarInputHandler/aih_constants.py


class ShakeReason(object):
    OWN_SHOT = 0
    OWN_SHOT_DELAYED = 1
    HIT = 2
    HIT_NO_DAMAGE = 3
    SPLASH = 4


class CTRL_MODE_NAME(object):
    ARCADE = 'arcade'
    STRATEGIC = 'strategic'
    SNIPER = 'sniper'
    POSTMORTEM = 'postmortem'
    DEBUG = 'debug'
    CAT = 'cat'
    VIDEO = 'video'
    MAP_CASE = 'mapcase'
    FALLOUT_DEATH = 'falloutdeath'
    DEFAULT = ARCADE


CTRL_MODES = (CTRL_MODE_NAME.ARCADE,
 CTRL_MODE_NAME.STRATEGIC,
 CTRL_MODE_NAME.SNIPER,
 CTRL_MODE_NAME.POSTMORTEM,
 CTRL_MODE_NAME.DEBUG,
 CTRL_MODE_NAME.CAT,
 CTRL_MODE_NAME.VIDEO,
 CTRL_MODE_NAME.MAP_CASE,
 CTRL_MODE_NAME.FALLOUT_DEATH)
GUN_MARKER_MIN_SIZE = 32.0
SPG_GUN_MARKER_ELEMENTS_COUNT = 37
SPG_GUN_MARKER_MIN_SIZE = 50.0
SPG_GUN_MARKER_MAX_SIZE = 100.0
SPG_GUN_MARKER_SCALE_RATE = 10.0

class GUN_MARKER_TYPE(int):
    UNDEFINED = 0
    CLIENT = 1
    SERVER = 2


class GUN_MARKER_FLAG(int):
    UNDEFINED = 0
    CONTROL_ENABLED = 1
    CLIENT_MODE_ENABLED = 2
    SERVER_MODE_ENABLED = 4
    VIDEO_MODE_ENABLED = 8
    ARTY_HIT_ENABLED = 16


class SHOT_RESULT(int):
    UNDEFINED = 0
    NOT_PIERCED = 1
    LITTLE_PIERCED = 2
    GREAT_PIERCED = 3
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\AvatarInputHandler\aih_constants.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:47:02 St�edn� Evropa (b�n� �as)
