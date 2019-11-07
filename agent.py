from game import Game
from evaluator import Evaluator


class Agent:

    def __init__(self, label):
        self.label = label
        self.debug = False
        self.evaluator = Evaluator()

    def move(self, game: Game, possible_moves=None):
        raise NotImplementedError("Subclasses should implement this!")

    def win(self):
        pass

    def draw(self):
        pass

    def loose(self):
        pass

    def new_game(self):
        pass

    def set_evaluaator(self, evaluator: Evaluator):
        self.evaluator = evaluator