from agent import Agent
from game import Game


class MinimaxWithAlphaBeta(Agent):

    def __init__(self, label, max_depth=10):
        super().__init__(label)
        self.max_depth = max_depth
        self.min_score = -max_depth
        self.max_score = max_depth

    def move(self, game: Game, possible_states=None):
        result = self.__minimax(game, 0, self.min_score, self.max_score, possible_states=possible_states)
        return result[0].state

    def __minimax(self, game: Game, depth, alpha, beta, is_my_turn=True, possible_states=None):

        winner = game.evaluate()
        if winner == self.label:
            return (game, self.max_score-depth)
        elif winner == 'draw':
            return (game, 0)
        elif winner is not None:
            return (game, self.min_score+depth)
        elif depth >= self.max_depth:
            my_label_index = [index for index in [0,1] if game.labels[index] == self.label][0]

            factor = ((-1)**depth) * (1 if my_label_index == 0 else -1)
            score = game.evaluate_heuristic()*factor
            if score > 0:
                score = score - depth
            elif score < 0:
                score = score + depth
            return (game, score)
        else:
            if possible_states is None:
                possible_states = game.get_possible_next_states()
            results = []
            for state in possible_states:
                game_clone = game.next_state_clone(state)
                result = self.__minimax(game_clone, depth + 1, alpha, beta, not is_my_turn)
                results.append((game_clone, result[1]))

                if is_my_turn and alpha < result[1]:
                    alpha = result[1]
                elif not is_my_turn and result[1] < beta:
                    beta = result[1]

                if alpha >= beta:
                    break

            if is_my_turn:
                final = max(results, key=lambda item: item[1])
            else:
                final = min(results, key=lambda item: item[1])
            return final
