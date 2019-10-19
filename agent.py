from game import Game


class Agent:

    def __init__(self, label):
        self.label = label
        self.debug = False

    def move(self, game: Game, possible_states=None):
        raise NotImplementedError("Subclasses should implement this!")

    def win(self):
        pass

    def draw(self):
        pass

    def loose(self):
        pass

    def new_game(self):
        pass
