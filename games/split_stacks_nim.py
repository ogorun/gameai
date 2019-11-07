from game import Game

class SplitStacksNim(Game):
    LABELS = ['1', '2']

    def __init__(self, stack_size=3):
        self.stack_size = stack_size
        super().__init__([self.stack_size], True)

    def is_final_state(self):
        for stack_size in self.state:
            if stack_size > 2:
                return False

        return True

    def evaluate(self):
        if not self.is_final_state():
            return None

        return self.labels[int(self.is_first_agent_turn)]

    def get_possible_next_states(self, limit=None):
        """

        :param limit: TODO: support limit ?
        :return:
        """
        moves = self.get_possible_moves(limit)
        states = [self.move_to_state(move) for move in moves]
        return states

    def move_to_state(self, move):
        index, part = move
        state_copy = self.state.copy()
        stack = state_copy.pop(index)
        state_copy.append(part)
        state_copy.append(stack-part)
        return state_copy

    def get_possible_moves(self, limit=None):
        return [(index, part) for index in range(len(self.state)) for part in range(1, self.state[index]//2+1)]

    def picture(self):
        print(self.state)