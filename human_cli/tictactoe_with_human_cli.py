from games import *
from agents import *
from evaluators import *
from agent_decorators.win_loose_decorator import WinLooseDecorator


player_X = HumanChessCliAgent('W')
#player_X = MinimaxWithAlphaBeta('X', max_depth=2)
#player_X.set_evaluaator(TicTacToeCheck2CombinationsEvaluator())
#player_X = WinLooseDecorator(SingleTreeDepthSensitiveMCSTAgent('X'))
#player_X.debug = True
player_O = HumanChessCliAgent('B')
#player_X.debug = True
#player_O = HumanSplitStacksNimCliAgent('2')

game = Chess()
game.debug = True
game.play([player_X, player_O])
print(game.evaluate())
