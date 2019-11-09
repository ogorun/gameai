from agents import *
from agents.win_loose_agent import WinLooseAgent
from games.split_stacks_nim import SplitStacksNim
from tqdm import tqdm
import gc

#player_X = RandomAgent('X')
player_X = WinLooseAgent(SingleTreeDepthSensitiveMCSTAgent('1'))
#player_X = MinimaxWithAlphaBeta('X')
#player_X = SingleTreeDepthSensitiveMCSTAgent('X', 1.41, 10, 10)
#player_O = DepthSensitiveMCSTAgent('O', 1.41, 10, 10)
#player_O = WinLooseDecorator(MinimaxWithAlphaBeta('O'))
#player_O = RandomAgent('2')
player_O =  WinLooseAgent(MinimaxWithAlphaBeta('2'))

#results = {'X': 0, 'O': 0, 'draw': 0}
results = {'1': 0, '2': 0, 'draw': 0}
for i in tqdm(range(100)):
    #start = time.time()
    ttt = SplitStacksNim(stack_size=10)
    #player_O.new_game()
    #player_X.new_game()
    #ttt.set_debug(True)
    ttt.play([player_X, player_O])
    result = ttt.evaluate()
    results[result] += 1
    #print('--------------------------')
    del ttt
    gc.collect()
    #print(f'game {i}: {time.time()-start}')

print(results)

# ttt = TicTacToe([player_O, player_X], ['X', 'O', 'O', 3, 'X', 5, 'X', 7, 'O'])
# ttt.set_debug(True)
# ttt.play()
# print(ttt.evaluate())
