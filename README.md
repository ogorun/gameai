# gameai

Repository for experiments with game agents.

## Games

TicTacToe

## Agents

| Algorithm | Description | Class |
| --------- | ----------- | ----- |
| Random | Agent returning random move from available, provided by game | RandomAgent |
| Minimax   | https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/ - classical variant. Depth first. Every game is proceeded to the end and evaluated with +10/0/-10 | MinimaxAgent |
| Depth sensitive minimax | Depth first. Every game is proceeded to the end. Game score depends on game final depth | DepthSensitiveMinimax |
| Minimax with alpha-beta pruning | https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/ . Every game is proceeded to the end. Game score depends on game final depth | MinimaxWithAlphaBeta |
| Monte Carlo Tree Search (MCTS) | https://www.geeksforgeeks.org/ml-monte-carlo-tree-search-mcts/ UCB is used for node choice. Every simulation is proceeded to the end and evaluated with +10/0/-10. MCTS tree is built for every move separately | MCTSAgent |
| Depth sensitive MCTS | Like above, but game score depends on final simulation game depth | DepthSensitiveMCTS |
| Single-tree depth sensitive MCTS | Like above, but the tree is not built from scratch on every move. Root is found if possible | SingleTreeDepthSensitiveMCTSAgent |

## Usage

Several scripts are provided for convenient work with these classes.

#### human_ai_game.py

This script provides interface way to play game vs automatic agent. Available agents are chosen from agent with names started with 'Human'.
Currently one such agent is implmented *HumanTicTacToeCliAgent*. It allows to play with a chosen automatic agent in TicTackToe through CLI interface.

~~~
python human_ai_game.py --help
usage: human_ai_game.py [-h] [-g {TicTacToe}] [-t {1,2}]
                        [--computer-agent {SingleTreeDepthSensitiveMCSTAgent,DepthSensitiveMCSTAgent,RandomAgent,MinimaxWithAlphaBeta,DepthSensitiveMinimaxAgent,MCSTAgent,MinimaxAgent}]
                        [--human-agent {HumanTicTacToeCliAgent}] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -g {TicTacToe}, --game {TicTacToe}
                        game class
  -t {1,2}, --turn {1,2}
                        human turn
  --computer-agent {SingleTreeDepthSensitiveMCSTAgent,DepthSensitiveMCSTAgent,RandomAgent,MinimaxWithAlphaBeta,DepthSensitiveMinimaxAgent,MCSTAgent,MinimaxAgent}
                        computer agent class
  --human-agent {HumanTicTacToeCliAgent}
                        human agent class
  -v, --verbosity       increase output verbosity

You can also add class parameters in format: --<class><param_type>.<param_name>=<param_value>

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

~~~  

### num_agents_games_comparison.py

This script provides way to compare two given agents efficiency on a specified game by playing N games (by default N=100).
At the end of the process the following metrics are provided: *general time*, *number of first agent wins*, *number of second agent wins*, 
*number of draws*

~~~

python num_agents_games_comparison.py --help
usage: num_agents_games_comparison.py [-h] [-g {TicTacToe}] [-n NUMBER]
                                      [--agent1 {SingleTreeDepthSensitiveMCSTAgent,DepthSensitiveMCSTAgent,RandomAgent,HumanTicTacToeCliAgent,MinimaxWithAlphaBeta,DepthSensitiveMinimaxAgent,MCSTAgent,MinimaxAgent}]
                                      [--agent2 {SingleTreeDepthSensitiveMCSTAgent,DepthSensitiveMCSTAgent,RandomAgent,HumanTicTacToeCliAgent,MinimaxWithAlphaBeta,DepthSensitiveMinimaxAgent,MCSTAgent,MinimaxAgent}]

optional arguments:
  -h, --help            show this help message and exit
  -g {TicTacToe}, --game {TicTacToe}
                        game class
  -n NUMBER, --number NUMBER
                        games number
  --agent1 {SingleTreeDepthSensitiveMCSTAgent,DepthSensitiveMCSTAgent,RandomAgent,HumanTicTacToeCliAgent,MinimaxWithAlphaBeta,DepthSensitiveMinimaxAgent,MCSTAgent,MinimaxAgent}
                        first agent class
  --agent2 {SingleTreeDepthSensitiveMCSTAgent,DepthSensitiveMCSTAgent,RandomAgent,HumanTicTacToeCliAgent,MinimaxWithAlphaBeta,DepthSensitiveMinimaxAgent,MCSTAgent,MinimaxAgent}
                        second agent class

You can also add class parameters in format: --<class><param_type>.<param_name>=<param_value>

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

~~~ 

## Testsets and algorithm comparison methods

Currently the following evaluation methods are used.

* Informal evaluation to get algorithm strength feeling by playing vs agent manually (*human_ai_game.py*)
* Formal evaluation by playing 100 games between two agents. Output metrics: *general time*, *number of first agent wins*, *number of second agent wins*, *number of draws* (script *num_agents_games_comparison.py*)

In the future, some domain-specific (for example, chess-specific) testing datasets can be introduced.

## Evaluation results

Comparison of agents work on N games (N = 100 most of time). Agents to compare are chosen the following way:

- Agent vs RandomAgent
- Agent vs itself
- Agent vs current best
- Specific interesting cases if any


| Game        | Agent1      |  Agent1 parameters | Agent2      | Agent2 parameters      | Games Number | Time (s)        | Agent1 Wins | Agent2 Wins | Draws | Comments |
| ----------- | ----------- | ------------------ | ----------- | ---------------------- | ------------ | --------------- | ----------- | ----------- | ----- | -------- |
| TicTacToe   | RandomAgent |                    | RandomAgent |                        | 100          | 1               | 62          | 24          | 14    |          |
| TicTacToe   | MinimaxAgent|                    | RandomAgent |                        | 100          | 2556 (42:36)    | 100         | 0           | 0     |          |
| TicTacToe   | MinimaxAgent|                    | MinimaxAgent|                        | 100          | 2755 (45:50)    | 0           | 0           | 100   | Strange that it's not twice Minmax/Random |
| TicTacToe   | DepthSensitiveMinimaxAgent|      | RandomAgent |                        | 100          | 2434 (40:34)    | 99          | 0           | 1     |          |
| TicTacToe   | DepthSensitiveMinimaxAgent|      | DepthSensitiveMinimaxAgent |         | 100          |     |          |            |      |          |
| TicTacToe   | DepthSensitiveMinimaxAgent|      | MinimaxAgent |                       | 100          |     |          |            |      |          |
| TicTacToe   | MinimaxWithAlphaBeta|            | RandomAgent |                        | 100          |     |          |            |      |          |
| TicTacToe   | MinimaxWithAlphaBeta|            | MinimaxWithAlphaBeta |               | 100          |     |          |            |      |          |
| TicTacToe   | MinimaxWithAlphaBeta|            | DepthSensitiveMinimaxAgent |         | 100          |     |          |            |      |          |
| TicTacToe   | MCSTAgent   | UCB1_const=1.41, trials_num=100 | RandomAgent |                        | 100          |     |          |            |      |          |
| TicTacToe   | MCSTAgent   | UCB1_const=1.41, trials_num=100 | MCSTAgent   |  UCB1_const=1.41, trials_num=100                        | 100          |     |          |            |      |          |
| TicTacToe   | MCSTAgent   | UCB1_const=1.41, trials_num=100 | MinimaxWithAlphaBeta |               | 100          |     |          |            |      |          |
| TicTacToe   | DepthSensitiveMCSTAgent|  UCB1_const=1.41, trials_num=100       | RandomAgent |                        | 100          |     |          |            |      |          |
| TicTacToe   | DepthSensitiveMCSTAgent| UCB1_const=1.41, trials_num=100  | DepthSensitiveMCSTAgent |  UCB1_const=1.41, trials_num=100         | 100          |     |          |            |      |          |
| TicTacToe   | DepthSensitiveMCSTAgent| UCB1_const=1.41, trials_num=100  | MCSTAgent |  UCB1_const=1.41, trials_num=100                       | 100          |     |          |            |      |          |
| TicTacToe   | DepthSensitiveMCSTAgent|  UCB1_const=1.41, trials_num=100      | MinimaxWithAlphaBeta |                       | 100          |     |          |            |      | With the best from different algorithm class (minimax)         |
| TicTacToe   | SingleTreeDepthSensitiveMCSTAgent| UCB1_const=1.41, trials_num=100       | RandomAgent |                        | 100          |     |          |            |      |          |
| TicTacToe   | SingleTreeDepthSensitiveMCSTAgent|  UCB1_const=1.41, trials_num=100      | SingleTreeDepthSensitiveMCSTAgent |  UCB1_const=1.41, trials_num=100         | 100          |     |          |            |      |          |
| TicTacToe   | SingleTreeDepthSensitiveMCSTAgent|  UCB1_const=1.41, trials_num=100      | DepthSensitiveMCSTAgent |  UCB1_const=1.41, trials_num=100                       | 100          |     |          |            |      |          |
| TicTacToe   | SingleTreeDepthSensitiveMCSTAgent|  UCB1_const=1.41, trials_num=100      | MinimaxWithAlphaBeta |                       | 100          |     |          |            |      | With the best from different algorithm class (minimax)         |
