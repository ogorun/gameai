from game import Game
from agent import Agent


class MinimaxAgent(Agent):

    def __init__(self, label):
        super().__init__(label)

    def move(self, game: Game):
        possible_states = game.get_possible_next_states()
        index =0 # random.randint(0, len(possible_states) - 1)
        return possible_states[index]

    def __minimax(self, game: Game):
        winner = game.evaluate()
        if winner == self.label:
            return 10
        elif winner is not None:
            return -10

