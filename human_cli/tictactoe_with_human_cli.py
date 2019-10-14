from agents.minimax_with_alpha_beta import MinimaxWithAlphaBeta
from agents.human_tictactoe_cli_agent import HumanTicTacToeCliAgent
from agents.mcst_agent import MCSTAgent
from games.tictactoe import TicTacToe

order = int(input('You play with O. Choose order: (1/2)?'))

#player_X = MinimaxWithAlphaBeta('X')
player_X = MCSTAgent('X', 1.41, 100, 10)
player_O = HumanTicTacToeCliAgent('O')

game = TicTacToe([player_O, player_X], None, order == 1)
game.set_debug(True)
game.play()
print(game.evaluate())
