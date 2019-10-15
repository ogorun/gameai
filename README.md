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

# TODO

### Games

- Divide stack into stacks of 2 and 1 - http://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15381-s06/www/gamesI.pdf
Isola - https://www.freecodecamp.org/news/playing-strategy-games-with-minimax-4ecb83b39b4b/
- Mancala
- checkers
- reversi
- Connect Four
- chess 

### Agents

- AlphaGO - https://www.analyticsvidhya.com/blog/2019/01/monte-carlo-tree-search-introduction-algorithm-deepmind-alphago/
- MCTS with enchancments:
   - fix bug +
   - score according to depth +/-
   - don't rebuild tree from scratch on every move
   - strateies to choose: the bigest value/n, the biggest UCB!, the biggest N
   - exclude loosing move, allways choose winning one,
   - exclude move followed by loosing, allways choose move followed by winning,
   - score according to depth with depth limit
   - score according to depth with time limit
   - search (Google) on "real-time MCTS"
- Transposition tables - http://mediocrechess.blogspot.com/2007/01/guide-transposition-tables.html
- Add networks for evaluation
   - (!) https://medium.com/@andreasstckl/writing-a-chess-program-in-one-day-30daff4610ec
   - (!) https://towardsdatascience.com/predicting-professional-players-chess-moves-with-deep-learning-9de6e305109e
   - https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/
   - https://appsilon.com/an-introduction-to-monte-carlo-tree-search/?nabc=1&nabe=4825491004194816:1&utm_referrer=https%3A%2F%2Fwww.google.com%2F
   - https://jeffbradberry.com/posts/2015/09/intro-to-monte-carlo-tree-search/
   - http://u.cs.biu.ac.il/~sarit/advai2018/MCTS.pdf
   - https://thesai.org/Downloads/Volume5No5/Paper_10-A_Comparative_Study_of_Game_Tree_Searching_Methods.pdf
   - https://skemman.is/bitstream/1946/9180/1/research-report.pdf
   - http://rin.io/chess-engine/
   - https://homepages.cwi.nl/~paulk/theses/Carolus.pdf
- NN
   - https://medium.com/applied-data-sci
   ence/how-to-build-your-own-alphazero-ai-using-python-and-keras-7f664945c188
   - https://int8.io/chess-position-evaluation-with-convolutional-neural-networks-in-julia/ with https://github.com/int8/chess-position-evaluation
   - https://bitbucket.org/waterreaction/giraffe/src/default/
   - http://blog.yhat.com/posts/deep-learning-chess.html
    - https://www.cs.tau.ac.il/~wolf/papers/deepchess.pdf + implementation in https://github.com/oripress/DeepChess

### Other features

- Add tree depth dictionary (compare 10/100 trials and depth independent vs depth dependent)
- Trace MC memory usage (is it swap problem)
- Profile MCTS
- Add seach tree graph
