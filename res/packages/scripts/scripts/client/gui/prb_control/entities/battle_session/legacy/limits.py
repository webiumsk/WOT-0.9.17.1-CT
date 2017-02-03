# 2017.02.03 21:48:38 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/prb_control/entities/battle_session/legacy/limits.py
from gui.prb_control.entities.base.limits import LimitsCollection, VehicleIsValid, VehiclesLevelLimit, TeamIsValid

class BattleSessionLimits(LimitsCollection):
    """
    Battle session limits class
    """

    def __init__(self, entity):
        super(BattleSessionLimits, self).__init__(entity, (VehicleIsValid(),), (VehiclesLevelLimit(), TeamIsValid()))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\battle_session\legacy\limits.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:38 Støední Evropa (bìžný èas)
