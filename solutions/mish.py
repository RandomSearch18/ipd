from random import random


class Strategy:
    def __init__(self):
        self.cooperate_for = 0

    def move(self, self_history: list[bool], opponent_history: list[bool]):
        def is_evil(history: list[bool]) -> bool:
            if len(history) < 3:
                return False
            for i in range(3):
                if history[i] is True:
                    return False
            return True

        def is_checkerboard() -> bool:
            # 4 seems like the optimal value here
            look_behind_len = 4
            if len(self_history) < look_behind_len:
                return False
            for i in range(look_behind_len):
                if self_history[-i] == opponent_history[-i]:
                    return False
            return True

        iteration = len(self_history)
        if iteration == 0:
            return True
        opponent_is_evil = is_evil(opponent_history)
        if opponent_is_evil:
            # No One Mourns The Wicked
            # (always defect if opponent looks like an always-defector)
            return False
        if is_checkerboard():
            # Try to break out of the checkerboard pattern that sometimes occurs with `joss`
            return True
        if self.cooperate_for:
            self.cooperate_for -= 1
            return True
        if opponent_history[-1] is False:
            # Probability of 0.1 or 0.2 seems optimal here
            if random() < 0.15:
                # Get scared and try cooperating for a bit
                self.cooperate_for = 2

        # Tit for tat:
        return opponent_history[-1]
