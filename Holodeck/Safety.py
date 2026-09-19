from .types import ActionType

class ActionSafetyGate:
    """Reject or bound actions before they reach the sandbox."""

    allowed = {
        ActionType.PULSE_FIELD,
        ActionType.INSERT_CATALYST,
        ActionType.CHANGE_TOPOLOGY,
        ActionType.MEASURE,
        ActionType.WAIT,
    }

    def validate(self, action: ActionType, magnitude: float = 0.0) -> bool:
        if action not in self.allowed:
            return False
        return abs(magnitude) <= 1.0

