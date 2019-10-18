from agents import *
from games.tictactoe import TicTacToe
from tqdm import tqdm
import gc
import time


#player_X = RandomAgent('X')
player_X = MCSTAgent('X', trials_num=10)
#player_X = SingleTreeDepthSensitiveMCSTAgent('X', 1.41, 10, 10)
#player_O = DepthSensitiveMCSTAgent('O', 1.41, 10, 10)
player_O = MCSTAgent('O', trials_num=10)

results = {'X': 0, 'O': 0, 'draw': 0}
for i in tqdm(range(1)):
    start = time.time()
    ttt = TicTacToe([player_X, player_O])
    #player_O.new_game()
    #player_X.new_game()
    #ttt.set_debug(True)
    ttt.play()
    result = ttt.evaluate()
    results[result] += 1
    #print('--------------------------')
    del ttt
    gc.collect()
    print(f'game {i}: {time.time()-start}')

print(results)

# ttt = TicTacToe([player_O, player_X], ['X', 'O', 'O', 3, 'X', 5, 'X', 7, 'O'])
# ttt.set_debug(True)
# ttt.play()
# print(ttt.evaluate())
