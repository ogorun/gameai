from agent import Agent
from games.tictactoe import TicTacToe


class HumanTicTacToeCliAgent(Agent):

    def move(self, game: TicTacToe, possible_steps=None):
        available = game.get_possible_next_steps()
        while True:
            choice = int(input('Your move? [0-8]'))
            if choice in available:
                return choice

            print('Not available')
