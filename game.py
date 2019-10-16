class Game:

    def __init__(self, agents, state=None, is_first_agent_turn=None, moves_limit=None):
        self.agents = agents
        self.state = state
        # self.turn = turn
        self.is_first_agent_turn = is_first_agent_turn
        self.moves_limit = moves_limit
        self.moves_num = 0
        self.debug = False

    def move(self, state):
        self.state = state
        if self.debug:
            self.picture()
        self.is_first_agent_turn = not self.is_first_agent_turn
        self.moves_num += 1

    def play(self):
        if self.debug:
            self.picture()
        while not self.is_final_state() and (self.moves_limit is None or self.moves_num > self.moves_limit):
            self.move(self.agents[int(not self.is_first_agent_turn)].move(self))

        winner = self.evaluate()
        for agent in self.agents:
            if agent.label == winner:
                agent.win()
            elif winner is 'draw':
                agent.draw()
            else:
                agent.loose()

    def is_final_state(self):
        pass

    def evaluate(self):
        return self.__evaluate(self.state, self.agents[int(not self.is_first_agent_turn)].label)

    def draw(self):
        pass

    def get_possible_next_states(self, limit=None):
        pass

    def picture(self):
        pass

    def state_hash(self):
        return self.state