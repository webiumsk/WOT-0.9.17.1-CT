# 2017.02.03 21:48:46 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/prb_control/entities/stronghold/unit/actions_validator.py
from UnitBase import ROSTER_TYPE
from gui.prb_control.entities.base.squad.actions_validator import UnitActionsValidator
from gui.prb_control.entities.base.unit.actions_validator import UnitVehiclesValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import UNIT_RESTRICTION
from shared_utils import findFirst

class StrongholdVehiclesValidator(UnitVehiclesValidator):

    def _validate(self):
        return super(StrongholdVehiclesValidator, self)._validate()


class StrongholdActionsValidator(UnitActionsValidator):

    def _createVehiclesValidator(self, entity):
        return StrongholdVehiclesValidator(entity)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\stronghold\unit\actions_validator.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:46 Støední Evropa (bìžný èas)
