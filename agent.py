from game import Game
from evaluator import Evaluator


class Agent:

    def __init__(self, label, agent=None):
        self.label = label
        self.debug = False
        self.agent = agent
        if self.agent is not None:
            self.agent.label = label

    def set_debug(self, debug):
        self.debug = debug
        if self.agent is not None:
            self.agent.set_debug(debug)

    def move(self, game: Game, possible_moves=None):
        raise NotImplementedError("Subclasses should implement this!")

    def win(self):
        pass

    def draw(self):
        pass

    def loose(self):
        pass

    def new_game(self):
        if self.agent is not None:
            self.agent.new_game()

    def set_evaluaator(self, evaluator: Evaluator):
        self.evaluator = evaluator