from game import Game
from games import *
from agent import Agent
from agents import *


order = int(input('You play with O. Choose order: (1/2)?'))

#player_X = MinimaxWithAlphaBeta('X')
player_X = SingleTreeDepthSensitiveMCSTAgent('X', 1.41, 100, 10)
#player_X.debug = True
player_O = HumanTicTacToeCliAgent('O')

game = TicTacToe([player_O, player_X], None, order == 1)
game.debug = True
game.play()
print(game.evaluate())
