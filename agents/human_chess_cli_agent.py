from agent import Agent
from games.chess import Chess
from chess import Move


class HumanChessCliAgent(Agent):

    def move(self, game: Chess, possible_steps=None):
        possible_steps = game.get_possible_next_steps()
        print(possible_steps)
        while True:
            try:
                choice = game.state.parse_san(input('Your move?'))
                print(choice)
                if choice in possible_steps:
                    return choice
            except ValueError as ex:
                print('Not available')
