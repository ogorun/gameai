from agent import Agent
from game import Game
from agents.random_agent import RandomAgent
import math, copy
from agents.mcst_node import MCSTTreeNode


class MCSTAgent(Agent):

    def __init__(self, label, UCB1_const=1.41, trials_num=100, steps_limit = 3):
        super().__init__(label)
        self.trials_num = trials_num
        self.steps_limit = steps_limit
        self.UCB_C = UCB1_const
        self.e = 0.000001

    def move(self, game: Game, possible_steps=None):
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
                    if possible_steps is not None and node.id == self.tree.id:
                        new_steps = possible_steps
                    else:
                        new_steps = node.game.get_possible_next_steps(self.steps_limit)
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
        tmp_game = copy.deepcopy(node.game)
        tmp_game.debug = False
        tmp_agents = [RandomAgent(label) for label in tmp_game.labels]
        tmp_game.play(tmp_agents)
        winner = tmp_game.evaluate()
        return self.winner2score(winner)

    def winner2score(self, winner):
        if winner == self.label:
            return 10
        elif winner == 'draw':
            return 0
        else:
            return -10

    def backpropogate(self, node, score):
        current_node = node
        while current_node is not None:
            current_node.n += 1
            current_node.s += score
            current_node = current_node.parent

    def choose_best_child(self):
        children_with_scores = [(node, node.s/(node.n + self.e)) for node in self.tree.children]
        return max(children_with_scores, key=lambda x: x[1])[0]
