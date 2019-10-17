from game import Game
from games import *
from agent import Agent
from agents import *
import argparse
import inspect


avaliable_games = [cls for cls in globals() if cls != 'Game' and inspect.isclass(globals()[cls]) and issubclass(globals()[cls], Game)]
avaliable_agents = [cls for cls in globals() if cls != 'Agent' and inspect.isclass(globals()[cls]) and issubclass(globals()[cls], Agent)]
human_agents = [agent for agent in avaliable_agents if agent.startswith('Human')]
ai_agents = [agent for agent in avaliable_agents if not agent.startswith('Human')]

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--game", help=f"Choose game. Available options: {', '.join(avaliable_games)}", default="TicTacToe")
parser.add_argument("-o", "--order", help=f"Choose order: (1/2)" , default="1")
parser.add_argument("--computer-agent", help=f"Choose computer agent. Available options: {', '.join(ai_agents)}", default="RandomAgent")
parser.add_argument("--human-agent", help=f"Choose computer agent. Available options: {', '.join(ai_agents)}", default="HumanTicTacToeCliAgent")
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
args = parser.parse_args()
print(args)

order = int(input('You play with O. Choose order: (1/2)?'))

#player_X = MinimaxWithAlphaBeta('X')
player_X = SingleTreeDepthSensitiveMCSTAgent('X', 1.41, 100, 10)
#player_X.debug = True
player_O = HumanTicTacToeCliAgent('O')
if args.verbosity:
    player_X.debug = True
    player_O.debug = True

game = TicTacToe([player_O, player_X], None, order == 1)
game.debug = True
game.play()
print(game.evaluate())
