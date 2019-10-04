from agents.random_agent import RandomAgent
from games.tictactoe import TicTacToe


player_X = RandomAgent('X')
player_O = RandomAgent('O')

for i in range(10):
    ttt = TicTacToe([player_X, player_O])
    ttt.set_debug(True)
    ttt.play()
    print(ttt.evaluate_itself())
