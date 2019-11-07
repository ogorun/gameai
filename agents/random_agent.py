from game import Game
from agent import Agent
import random


class RandomAgent(Agent):

    def move(self, game: Game, possible_steps=None):
        if possible_steps is None:
            possible_steps = game.get_possible_next_steps()
        index = random.randint(0, len(possible_steps) - 1)
        return possible_steps[index]

