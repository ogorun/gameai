from agent import Agent
from game import Game


class HumanTicTacToeCliAgent(Agent):

    def move(self, game: Game, possible_states=None):
        available = game.get_possible_next_states()
        while True:
            choice = int(input('Your move? [0-8]'))
            state = game.state.copy()
            if choice >=0 and choice < 9:
                state[choice] = self.label
                if state in available:
                    return state

            print('Not available')
