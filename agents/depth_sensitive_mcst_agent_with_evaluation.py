from agent import Agent
from agents.random_agent import RandomAgent
from agents.heuristic_agent import HeuristicAgent
import math, copy
import gc
from agents.mcst_node import MCSTTreeNode


class DepthSensitiveMCSTAgentWithEvaluation(Agent):

    def __init__(self, label, UCB1_const=1.41, trials_num=100, states_limit=3, evaluator=None):
        super().__init__(label)
        self.trials_num = trials_num
        self.states_limit = states_limit
        self.UCB_C = UCB1_const
        self.e = 0.000001
        self.evaluator = evaluator

    def move(self, game, possible_steps=None):
        if hasattr(self, 'tree'):
            del self.tree
            gc.collect()

        self.tree = MCSTTreeNode(game)

        for trial in range(self.trials_num):
            node = self.select(possible_steps)
            result = self.simulate(node)
            self.backpropogate(node, result)
            if self.debug:
                self.tree.draw(f"{self.label} - {game.moves_num} - {trial}")

        chosen_node = self.choose_best_child()
        if self.debug:
            print(self.tree.leafs_counter())
        return chosen_node.step

    def select(self, possible_steps=None):
        node = self.tree
        while True:
            if node.is_leaf():
                if node.n == 0 and node.id != self.tree.id or node.game.is_final_state(): # new node
                    return node
                else:
                    if node.id == self.tree.id and possible_steps is not None:
                        new_steps = possible_steps
                    else:
                        new_steps = node.game.get_possible_next_steps(self.states_limit)
                    for step in new_steps:
                        new_game = node.game.copy_and_move(step)
                        node.append(MCSTTreeNode(new_game, step))
                    return node.children[0]
            else:
                ucb1_scores = [(n, self.ucb1(n)) for n in node.children]
                node = max(ucb1_scores, key=lambda x: x[1])[0]

    def ucb1(self, node: MCSTTreeNode):
        return node.s + self.UCB_C * math.sqrt(math.log(node.parent.n)/(node.n + self.e))

    def simulate(self, node: MCSTTreeNode):
        return self.evaluator.evaluate(node.game)

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
