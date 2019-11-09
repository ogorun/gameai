from evaluator import Evaluator
from agent import Agent
from game import Game


class HeuristicAgent(Agent):

    def __init__(self, label, evaluator: Evaluator):
        super().__init__(label)
        self.evaluator = evaluator

    def move(self, game: Game, possible_moves=None):
        my_label_index = [index for index in [0,1] if game.labels[index] == self.label][0]
        factor = (1 if my_label_index == 0 else -1)
        possible_moves = game.get_possible_next_steps()
        results = [(step, self.evaluator.evaluate(game.copy_and_move(step))*factor) for step in possible_moves]
        return max(results, key=lambda item: item[1])[0]
