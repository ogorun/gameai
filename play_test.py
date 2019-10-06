from agents.random_agent import RandomAgent
from agents.minimax_agent import MinimaxAgent
from agents.depth_sensitive_minimax_agent import DepthSensitiveMinimaxAgent
from agents.minimax_with_alpha_beta import MinimaxWithAlphaBeta
from games.tictactoe import TicTacToe
from tqdm import tqdm


#player_X = RandomAgent('X')
player_X = MinimaxWithAlphaBeta('X')
player_O = MinimaxWithAlphaBeta('O')

results = {'X': 0, 'O': 0, 'draw': 0}
for i in tqdm(range(100)):
    ttt = TicTacToe([player_X, player_O])
    #ttt.set_debug(True)
    ttt.play()
    result = ttt.evaluate()
    results[result] += 1
    #print('--------------------------')

print(results)

# ttt = TicTacToe([player_O, player_X], ['O', 1, 'X', 3, 4, 5, 6, 7, 'X'])
# ttt.set_debug(True)
# ttt.play()
# print(ttt.evaluate())
