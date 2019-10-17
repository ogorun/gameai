class Game:
    """
    A base class used to represent a Game.
    The following restrictions are supposed:
    * It's a game for strictly two players
    * fully observable
    * deterministic
    * discrete
    * adversarial
    There are three possible outcomes: first player wins, second player wins, draw.
    For every concrete game type separate class should be implemented. It should define functionality related to game state and possible moves.

    Attributes
    ----------

    agents (list of 2 Agent objects)
        - Game players are represented by agents that are responsible of move choice
    state
        - Concrete state representation is domain-specific and should be defined in derived classes
    is_first_agent_turn (bool)
        - Current turn indicator
    moves_num (int)
        - Number of currently made mmoves. NB: *moves_num* is incremented after every agent step. So if given value is moves_num
          every agent did either moves_num/2 or moves_num/2-1 steps.
    moves_limit (int or None)
        - Limit of moves number. The game is ended if its state is terminal of moved_limit is exceeded.
    debug (bool)
        - debug flag. Used to draw game board

    Methods
    -------

    move(state)
        - makes move to the given state

    play()
        - plays game calling agent move() method till the game is finished

    is_final_state()
        - checks whether game is finished. Should be redefined by child class

    evaluate()
        - evaluates the game state. Actual evaluation is done in child classs
         TBD: current classes return winner label or 'draw'. Maybe it should be redefined
          to return numerical estimation, and not only for final state

    get_possible_next_states(limit)
        - returns possible next states. Should be implemented in child class

    picture()
        - draws board. Should be implemented in child class

    state_hash()
        - returns state hash for comparison by agents

    """

    def __init__(self, agents, state=None, is_first_agent_turn=None, moves_limit=None):
        """
        Constructor

        :param agents: Game players are represented by agents that are responsible of move choice
        :param state: Concrete state representation is domain-specific and should be defined in derived classes.
                    Game can be started from any state that can be provided manually. Otherwise initial game state should be defined in derived classes
        :param is_first_agent_turn: Since at game initialisation the state is not necessary initial state, turn is also not necessary the default one.
                    Boolean value
        :param moves_limit: - limit of game moves number
        """

        self.agents = agents
        self.state = state
        self.is_first_agent_turn = is_first_agent_turn
        self.moves_limit = moves_limit
        self.moves_num = 0
        self.debug = False

        self.agents[0].new_game()
        self.agents[1].new_game()

    def move(self, state):
        """
        Makes move to the given state

        :param state:
        """

        self.state = state
        if self.debug:
            self.picture()
        self.is_first_agent_turn = not self.is_first_agent_turn
        self.moves_num += 1

    def play(self):
        """
        Plays game calling agent move() method till the game is finished
        """

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

    # def draw(self):
    #     pass

    def get_possible_next_states(self, limit=None):
        """

        :param limit: TODO: support limit ?
        :return:
        """
        pass

    def picture(self):
        """

        TODO: probably separate drawing to classes responsible of presentation level
        :return:
        """
        pass

    def state_hash(self):
        return self.state
