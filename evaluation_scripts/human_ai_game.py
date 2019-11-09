from game import Game
from games import *
from agent import Agent
from agents import *
import argparse, inspect, re


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def add_parser_argument(parser, arg):
    if arg.startswith('--c') or arg.startswith('--h') or arg.startswith('--g') and arg[3] in ['i', 'f', 'b', 's']:
        argtype = None
        if arg[3] == 'i':
            argtype = int
        elif arg[3] == 'f':
            argtype = float
        elif arg[3] == 'b':
            argtype = str2bool
        else:
            argtype = str

        argname, argvalue = arg.split('=', 1)

        parser.add_argument(argname, type=argtype)


def instantiate_agent_from_params(args, class_name, param_prefix, label):
    agent_cls = globals()[args[class_name]]
    agent_params = {key[3:]: val for key, val in args.items() if re.match(f'^{param_prefix}(i|f|b|s_\.)', key)}
    agent = agent_cls(label, **agent_params)
    return agent


avaliable_games = [cls for cls in globals() if cls != 'Game' and inspect.isclass(globals()[cls]) and issubclass(globals()[cls], Game)]
avaliable_agents = [cls for cls in globals() if cls != 'Agent' and inspect.isclass(globals()[cls]) and issubclass(globals()[cls], Agent)]
human_agents = [agent for agent in avaliable_agents if agent.startswith('Human')]
ai_agents = [agent for agent in avaliable_agents if not agent.startswith('Human')]

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""You can also add class parameters in format: --<class><param_type>.<param_name>=<param_value>

They will be passed to corresponding class at initialization.

<class> allows the following values:
c - computer agent class
h - human agent class
g - game class.

<param_type> allows the following values:
f - float
i - integer
b - boolean
s - string

Example: --ci.trials_num=100. Integer paramete trials_num=100 will be passed to constructor of class, specified by --computer-agent parameter

Unknwon parameters that don't follow described pattern will be ignored.

""")
parser.add_argument("-g", "--game", help=f"game class", choices=avaliable_games, default="TicTacToe")
parser.add_argument("-t", "--turn", type=int, help=f"human turn" , choices=[1,2], default="1")
parser.add_argument("--computer-agent", help=f"computer agent class", choices=ai_agents, default="RandomAgent")
parser.add_argument("--human-agent", help=f"human agent class", choices=human_agents, default="HumanTicTacToeCliAgent")
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")


parsed, unknown = parser.parse_known_args()
for arg in unknown:
    add_parser_argument(parser, arg)

args = vars(parser.parse_args())
print(args)

game_cls = locals()[args['game']]
game_params = {key[3:]: val for key, val in args.items() if re.match(f'^g(i|f|b|s_\.)', key)}

human_agent = instantiate_agent_from_params(args, 'human_agent', 'h', game_cls.LABELS[args['turn']-1])
ai_agent = instantiate_agent_from_params(args, 'computer_agent', 'c', game_cls.LABELS[1 - (args['turn']-1)])

agents = [None, None]
agents[args['turn']-1] = human_agent
agents[1 - (args['turn']-1)] = ai_agent

game = game_cls(**game_params)
game.debug = True
if args['verbosity']:
    for agent in game.agents:
        agent.set_debug(True)

print(f'You play {human_agent.label}')
game.play(agents)
print(game.evaluate())
