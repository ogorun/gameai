from agents.random_agent import RandomAgent
from agents.minimax_agent import MinimaxAgent
from games.tictactoe import TicTacToe
from tqdm import tqdm


player_X = MinimaxAgent('X')
player_O = MinimaxAgent('O')

results = {'X': 0, 'O': 0, 'draw': 0}
for i in tqdm(range(100)):
    ttt = TicTacToe([player_X, player_O])
    #ttt.set_debug(True)
    ttt.play()
    result = ttt.evaluate()
    results[result] += 1

print(results)

# ttt = TicTacToe([player_O, player_X], ['O', 'X', 'O', 'X', 'O', 'X', 'X', 7, 8])
# ttt.set_debug(True)
# ttt.play()
# print(ttt.evaluate())