from game import Game


class TicTacToe(Game):

    def __init__(self, agents, state=None, is_first_agent_turn=None):
        agents, state, turn = self.__validate_initialization(agents, state, is_first_agent_turn)
        super().__init__(agents, state, turn)

    def __validate_initialization(self, agents, state, is_first_agent_turn):

        is_x_found = is_o_found = False
        for agent in agents:
            if agent.label == 'X':
                is_x_found = True
            elif agent.label == 'O':
                is_o_found = True
            else:
                raise Exception("Invalid agent")

        if not is_x_found or not is_o_found:
            raise Exception("Invalid agents")

        is_first_agent_turn = True if is_first_agent_turn not in [True, False] else is_first_agent_turn
        state = [0, 1, 2, 3, 4, 5, 6, 7, 8] if state is None else state

        if len(state) != 9:
            raise Exception('Invalid state')

        return agents, state, is_first_agent_turn

    def is_final_state(self):
        return (self.evaluate() is not None)

    def evaluate(self):
        return self.__evaluate(self.state, self.agents[int(not self.is_first_agent_turn)].label)

    def __evaluate(self, state, turn):
        lines = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        for line in lines:
            if state[line[0]] == state[line[1]] == state[line[2]]:
                return state[line[0]]

        not_filled = self.__find_not_filled(state)
        if len(not_filled) == 0:
            return 'draw'

        return None

    def picture(self):
        print('===')
        for row in range(0,3):
            str = ''
            for col in range(0,3):
                index = row*3+col
                str += ' ' if type(self.state[index]) == int else self.state[index]
            print(str)
        print('===')

    @staticmethod
    def __find_not_filled(state):
        return [field for field in state if type(field) == int]

    def get_possible_next_states(self, limit=None):
        not_filled = self.__find_not_filled(self.state)
        states = []
        for field in not_filled:
            state = self.state.copy()
            state[field] = self.agents[int(not self.is_first_agent_turn)].label
            states.append(state)
        return states
