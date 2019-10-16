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

TBD

## Testsets and algorithm comparison methods

TBD

## Evaluation results

TBD

