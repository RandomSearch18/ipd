from random import random


class Strategy:
    def __init__(self):
        self.cooperate_for = 0

    def move(self, self_history: list[bool], opponent_history: list[bool]):
        iteration = len(self_history)
        if iteration == 0:
            return True
        # opponent_is_evil =
        if self.cooperate_for:
            self.cooperate_for -= 1
            return True
        if opponent_history[-1] is False:
            if random() < 0.1:
                # Get scared and try cooperating for a bit
                self.cooperate_for = 2

        # Tit for tat:
        return opponent_history[-1]
