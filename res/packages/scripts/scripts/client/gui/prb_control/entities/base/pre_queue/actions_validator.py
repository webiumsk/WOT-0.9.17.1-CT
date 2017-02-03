# 2017.02.03 21:48:32 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/base/pre_queue/actions_validator.py
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator, ActionsValidatorComposite, CurrentVehicleActionsValidator
from gui.prb_control.items import ValidationResult

class InQueueValidator(BaseActionsValidator):
    """
    Is player in queue validator.
    """

    def _validate(self):
        if self._entity.isInQueue():
            return ValidationResult(False)
        return super(InQueueValidator, self)._validate()


class PreQueueActionsValidator(ActionsValidatorComposite):
    """
    Pre queue actions validator base class.
    """

    def __init__(self, entity):
        validators = [InQueueValidator(entity), CurrentVehicleActionsValidator(entity)]
        super(PreQueueActionsValidator, self).__init__(entity, validators)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\base\pre_queue\actions_validator.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:48:32 St�edn� Evropa (b�n� �as)
