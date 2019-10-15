from agents.random_agent import RandomAgent
from agents.minimax_agent import MinimaxAgent
from agents.depth_sensitive_minimax_agent import DepthSensitiveMinimaxAgent
from agents.minimax_with_alpha_beta import MinimaxWithAlphaBeta
from agents.mcst_agent import MCSTAgent
from agents.depth_sensitive_mcst_agent import DepthSensitiveMCSTAgent
from games.tictactoe import TicTacToe
from tqdm import tqdm
import gc


#player_X = RandomAgent('X')
#player_X = MinimaxWithAlphaBeta('X')
player_X = DepthSensitiveMCSTAgent('X', 1.41, 10, 10)
player_O = DepthSensitiveMCSTAgent('O', 1.41, 10, 10)

results = {'X': 0, 'O': 0, 'draw': 0}
for i in tqdm(range(100)):
    ttt = TicTacToe([player_X, player_O])
    #ttt.set_debug(True)
    ttt.play()
    result = ttt.evaluate()
    results[result] += 1
    #print('--------------------------')
    del ttt
    gc.collect()

print(results)

# ttt = TicTacToe([player_O, player_X], ['X', 'O', 'O', 3, 'X', 5, 'X', 7, 'O'])
# ttt.set_debug(True)
# ttt.play()
# print(ttt.evaluate())
