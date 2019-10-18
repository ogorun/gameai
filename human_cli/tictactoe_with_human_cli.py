from game import Game
from games import *
from agent import Agent
from agents import *


order = int(input('You play with O. Choose order: (1/2)?'))

#player_X = MinimaxWithAlphaBeta('X')
player_X = MCSTAgent('X', 1.41, 100, 10)
#player_X.debug = True
player_O = HumanTicTacToeCliAgent('O')

game = TicTacToe(is_first_agent_turn=(order == 2))
game.debug = True
game.play([player_X, player_O])
print(game.evaluate())
