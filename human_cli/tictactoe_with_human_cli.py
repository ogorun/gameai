from games import *
from agents import *
from agent_decorators.win_loose_decorator import WinLooseDecorator


order = int(input('You play with O. Choose order: (1/2)?'))

#player_X = MinimaxWithAlphaBeta('X')
player_X = WinLooseDecorator(SingleTreeDepthSensitiveMCSTAgent('X'))
player_X.debug = True
player_O = HumanTicTacToeCliAgent('O')

game = TicTacToe(is_first_agent_turn=(order == 2))
game.debug = True
game.play([player_X, player_O])
print(game.evaluate())
