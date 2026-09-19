from .types import ActionType

class ProtectiveAgent:
    """Minimal baseline controller: WATCH during high separation."""

    def __init__(self, enter=0.78, exit=0.62):
        self.enter = enter
        self.exit = exit
        self.in_regime = False

    def choose(self, separation_score: float):
        if not self.in_regime and separation_score >= self.enter:
            self.in_regime = True
        elif self.in_regime and separation_score < self.exit:
            self.in_regime = False

        if self.in_regime:
            return ActionType.WAIT
        return ActionType.WAIT

