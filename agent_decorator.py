from agent import Agent
from game import Game


class AgentDecorator(Agent):

    def __init__(self, agent: Agent):
        super().__init__(agent.label)
        self.agent = agent

    def move(self, game: Game, possible_states=None):
        raise NotImplementedError("Subclasses should implement this!")

    def new_game(self):
        self.agent.new_game()

    #def __getattr__(self, item):
    #    if not hasattr(self, name):
    #       return self.agent.__getattribute__(item)