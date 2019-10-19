from game import Game
from games import *
from agent import Agent
from agents import *
from tqdm import tqdm
import argparse, inspect, re, time, gc

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
    if arg.startswith('--a1') or arg.startswith('--a2') or arg.startswith('--g') and arg[3] in ['i', 'f', 's', 'b']:
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


def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue


def instantiate_agent_from_params(args, class_name, param_prefix, label):
    agent_cls = globals()[args[class_name]]
    agent_params = {key[4:]: val for key, val in args.items() if re.match(f'^{param_prefix}(i|f|b|s_\.)', key)}
    agent = agent_cls(label, **agent_params)
    return agent


avaliable_games = [cls for cls in globals() if cls != 'Game' and inspect.isclass(globals()[cls]) and issubclass(globals()[cls], Game)]
avaliable_agents = [cls for cls in globals() if cls != 'Agent' and inspect.isclass(globals()[cls]) and issubclass(globals()[cls], Agent)]

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""You can also add class parameters in format: --<class><param_type>.<param_name>=<param_value>

They will be passed to corresponding class at initialization.

<class> allows the following values:
a1 - first agent class
a2 - second agent class
g - game class.

<param_type> allows the following values:
f - float
i - integer
b - boolean
s - string

Example: --a1i.trials_num=100. Integer paramete trials_num=100 will be passed to constructor of class, specified by --agent1 parameter

Unknwon parameters that don't follow described pattern will be ignored.

""")
parser.add_argument("-g", "--game", help=f"game class", choices=avaliable_games, default="TicTacToe")
parser.add_argument("-n", "--number", type=positive_int, help=f"games number", default=100)
parser.add_argument("--agent1", help=f"first agent class", choices=avaliable_agents, default="RandomAgent")
parser.add_argument("--agent2", help=f"second agent class", choices=avaliable_agents, default="RandomAgent")

parsed, unknown = parser.parse_known_args()
for arg in unknown:
    add_parser_argument(parser, arg)

args = vars(parser.parse_args())
print(args)

game_cls = locals()[args['game']]
game_params = {key[3:]: val for key, val in args.items() if re.match(f'^g(i|f|b|s_\.)', key)}

agents = [
    instantiate_agent_from_params(args, 'agent1', 'h', game_cls.LABELS[0]),
    instantiate_agent_from_params(args, 'agent2', 'c', game_cls.LABELS[1])
]

results = {game_cls.LABELS[0]: 0, game_cls.LABELS[1]: 0, 'draw': 0}
for i in tqdm(range(args['number'])):
    #start = time.time()
    game = game_cls(**game_params)
    game.play(agents)
    result = game.evaluate()
    results[result] += 1
    del game
    gc.collect()
    #print(time.time()-start)

print(results)

