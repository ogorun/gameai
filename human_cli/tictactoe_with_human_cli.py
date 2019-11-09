from games import *
from agents import *
from evaluators import *
from agent_decorators.win_loose_decorator import WinLooseDecorator


player_1 = HeuristicAgent('W', evaluator=MaterialPositionChessEvaluator())
#player_X = MinimaxWithAlphaBeta('X', max_depth=2)
#player_X.set_evaluaator(TicTacToeCheck2CombinationsEvaluator())
#player_X = WinLooseDecorator(SingleTreeDepthSensitiveMCSTAgent('X'))
#player_X.debug = True
player_2 = HumanChessCliAgent('B')
#player_X.debug = True
#player_O = HumanSplitStacksNimCliAgent('2')

game = Chess()
game.debug = True
game.play([player_1, player_2])
print(game.evaluate())
