from game import Game
from agent import Agent
import random


class RandomAgent(Agent):

    def __init__(self, label):
        super().__init__(label)

    def move(self, game: Game):
        possible_states = game.get_possible_next_states()
        index = random.randint(0, len(possible_states) - 1)
        return possible_states[index]

