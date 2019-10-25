from game import Game


class TicTacToe(Game):
    LABELS = ['X', 'O']
    MAX_SCORE = 100

    def __init__(self, state=None, is_first_agent_turn=None):
        state, turn = self.__validate_initialization(state, is_first_agent_turn)
        super().__init__(state, turn)

    def __validate_initialization(self, state, is_first_agent_turn):
        is_first_agent_turn = True if is_first_agent_turn not in [True, False] else is_first_agent_turn
        state = [0, 1, 2, 3, 4, 5, 6, 7, 8] if state is None else state

        if len(state) != 9:
            raise Exception('Invalid state')

        return state, is_first_agent_turn

    def is_final_state(self):
        return (self.evaluate() is not None)

    def evaluate(self):
        return self.__evaluate(self.state, self.labels[int(self.is_first_agent_turn)])

    def __evaluate(self, state, turn):
        winner = self.check_three_in_line(state)
        if winner is not None:
            return winner

        not_filled = self.__find_not_filled(state)
        if len(not_filled) == 0:
            return 'draw'

        return None

    def evaluate_heuristic(self):
        for field in [0,2,4,6,8]:
            if type(self.state[field]) == int:
                return 1 * (1 if self.is_first_agent_turn else -1)

        return 0


    # def evaluate_heuristic(self):
    #     evaluate_as_final = self.evaluate()
    #     if evaluate_as_final is not None:
    #         return evaluate_as_final
    #
    #     past_turn_label = self.labels[int(not self.is_first_agent_turn)]
    #     next_turn_label = [label for label in self.LABELS if label != past_turn_label][0]
    #     sign = 1 if self.is_first_agent_turn else -1
    #
    #     possible_states = self.get_possible_next_states()
    #     next_state_count_lines = []
    #     # opposite 3 in line on next move - -100
    #     for next_state in possible_states:
    #         game_clone = self.next_state_clone(next_state)
    #         next_state_count_lines.append(game_clone.count_lines(next_state))
    #         if next_state_count_lines[-1][3][next_turn_label] > 0:
    #             return -100*sign
    #
    #     state_count_lines = self.count_lines(self.state)
    #
    #     # fork (2 in line twice) - 50
    #     if state_count_lines[2][past_turn_label] == 2:
    #         return 50*sign
    #
    #     # opposite fork (2 in line twice) on next move  - -50
    #     for counter in next_state_count_lines:
    #         # TODO: This condition will miss 2 in line blocked by next fork
    #         if counter[2][next_turn_label] == 2 and state_count_lines[2][past_turn_label] == 0:
    #             return -50*sign
    #
    #     # 2 in line - 20
    #     if state_count_lines[2][past_turn_label] > 0:
    #         return 20*sign
    #
    #     # opposite 2 in line on next move - -20
    #     for counter in next_state_count_lines:
    #         if counter[2][next_turn_label] > 0:
    #             return -20*sign
    #
    #     # default - 0
    #     return 0

    def check_three_in_line(self, state):
        lines = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        for line in lines:
            if state[line[0]] == state[line[1]] == state[line[2]]:
                return state[line[0]]

        return None

    def count_lines(self, state):
        lines = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        label_count = {3: {'X': 0, 'O': 0}, 2: {'X':0, 'O': 0}}
        line_label_counts = [
            {'X': 0, 'O': 0},
            {'X': 0, 'O': 0},
            {'X': 0, 'O': 0},
            {'X': 0, 'O': 0},
            {'X': 0, 'O': 0},
            {'X': 0, 'O': 0},
            {'X': 0, 'O': 0},
            {'X': 0, 'O': 0},
            {'X': 0, 'O': 0}
        ]
        for index, line in enumerate(lines):
            for i in range(3):
                if type(state[line[i]]) == str:
                    line_label_counts[index][state[line[i]]] += 1
            for sign in ['X','O']:
                second_sign = 'X' if sign == 'O' else 'O'
                if line_label_counts[index][sign] == 3:
                    label_count[3][sign] += 1
                elif line_label_counts[index][sign] == 2 and line_label_counts[index][second_sign] == 0:
                    label_count[2][sign] += 1

        return label_count


    def picture(self):
        print('===')
        for row in range(0,3):
            str = ''
            for col in range(0,3):
                index = row*3+col
                str += '-' if type(self.state[index]) == int else self.state[index]
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
            state[field] = self.labels[int(not self.is_first_agent_turn)]
            states.append(state)
        return states
