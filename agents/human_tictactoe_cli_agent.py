from agent import Agent
from game import Game


class HumanTicTacToeCliAgent(Agent):

    def move(self, game: Game):
        available = game.get_possible_next_states()
        while True:
            choice = int(input('Your move? [0-8]'))
            state = game.state.copy()
            state[choice] = self.label
            if state in available:
                return state
            else:
                print('Not available')
