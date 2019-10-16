from agent import Agent
from game import Game
from agents.random_agent import RandomAgent
import math, copy
import gc
from agents.mcts_node import MCSTTreeNode



class SingleTreeDepthSensitiveMCSTAgent(Agent):

    def __init__(self, label, UCB1_const, trials_num, states_limit = 3):
        super().__init__(label)
        self.trials_num = trials_num
        self.states_limit = states_limit
        self.UCB_C = UCB1_const
        self.e = 0.000001

    def move(self, game: Game):
        self.reset_tree(game)

        for trial in range(self.trials_num):
            node = self.select()
            result = self.simulate(node)
            self.backpropogate(node, result)
            if self.debug:
                self.tree.draw(f"{self.label} - {game.moves_num} - {trial}")

        self.chosen_node = self.choose_best_child()
        if self.debug:
            print(self.tree.leafs_counter())

        return self.chosen_node.game.state

    def reset_tree(self, game):
        node = None
        if hasattr(self, 'chosen_node'):
            node = self.chosen_node.find_game_node(game)
            if node is None:
                node = MCSTTreeNode(copy.deepcopy(game))
                self.chosen_node.append(node)
            else:
                print('found!!!!!!', len(node.children))
            self.tree.prune_tree_with_node(node)
            self.tree.draw('prunned')
        else:
            node = MCSTTreeNode(copy.deepcopy(game))

        self.tree = node
        gc.collect()

    def select(self):
        node = self.tree
        while True:
            if node.is_leaf():
                if node.n == 0 and node.id != self.tree.id or node.game.is_final_state(): # new node
                    return node
                else:
                    new_states = node.game.get_possible_next_states(self.states_limit)
                    for state in new_states:
                        new_game = copy.deepcopy(node.game)
                        new_game.debug = False
                        new_game.move(state)
                        node.append(MCSTTreeNode(new_game))
                    return node.children[0]
            else:
                ucb1_scores = [(n, self.ucb1(n)) for n in node.children]
                node = max(ucb1_scores, key=lambda x: x[1])[0]

    def ucb1(self, node: MCSTTreeNode):
        return node.s + self.UCB_C * math.sqrt(math.log(node.parent.n)/(node.n + self.e))

    def simulate(self, node: MCSTTreeNode):
        tmp_game = copy.deepcopy(node.game)
        tmp_game.debug = False
        tmp_agents = [RandomAgent(agent.label) for agent in tmp_game.agents]
        tmp_game.agents = tmp_agents
        tmp_game.play()
        winner = tmp_game.evaluate()
        return self.winner2score(winner, tmp_game.moves_num - self.tree.depth())

    def winner2score(self, winner, moves_num):
        if winner == self.label:
            return 10-moves_num
        elif winner == 'draw':
            return 0
        else:
            return -(10-moves_num)

    def backpropogate(self, node, score):
        current_node = node
        while current_node is not None:
            current_node.n += 10
            current_node.s += score
            current_node = current_node.parent

    def choose_best_child(self):
        children_with_scores = [(node, node.s/(node.n + self.e)) for node in self.tree.children]
        return max(children_with_scores, key=lambda x: x[1])[0]
