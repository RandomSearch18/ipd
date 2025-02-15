class Strategy:
    def __init__(self):
        self.sneaky = False
        self.cooperate_for = 0

    def move(self, self_history: list[bool], opponent_history: list[bool]):
        iteration = len(self_history)
        if iteration == 0:
            return True
        if iteration == 15:
            # At iteration 15, get bored and try exploiting the opponent
            # self.sneaky = True
            pass
        if self.cooperate_for:
            self.cooperate_for -= 1
            return True
        if self.sneaky:
            # Try to be sneaky and exploit the opponent
            return False
        if opponent_history[-1] is False:
            # Too scared to try to be sneaky
            self.sneaky = False
            self.cooperate_for = 2

        # Tit for tat:
        return opponent_history[-1]
