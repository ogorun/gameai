from games import *
from agents import *
from evaluators import *

player_1 = WinLooseAgent('W', HeuristicAgent('W', evaluator=MaterialPositionChessEvaluator()))
#player_X = MinimaxWithAlphaBeta('X', max_depth=2)
#player_X.set_evaluaator(TicTacToeCheck2CombinationsEvaluator())
#player_X = WinLooseDecorator(SingleTreeDepthSensitiveMCSTAgent('X'))
#player_X.set_debug(True)
player_2 = HumanChessCliAgent('B')
#player_O = HumanSplitStacksNimCliAgent('2')

game = Chess()
game.debug = True
game.play([player_1, player_2])
print(game.evaluate())
