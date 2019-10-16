from agent import Agent
from game import Game
import copy


class MinimaxWithAlphaBeta(Agent):

    def __init__(self, label, max_depth=10):
        super().__init__(label)
        self.max_depth = max_depth
        self.min_score = -max_depth
        self.max_score = max_depth

    def move(self, game: Game):
        result = self.__minimax(game, 0, self.min_score, self.max_score)
        return result[0].state

    def __minimax(self, game: Game, depth, alpha, beta, is_my_turn=True):
        winner = game.evaluate()
        if winner == self.label:
            return (game, self.max_score-depth)
        elif winner == 'draw':
            return (game, 0)
        elif winner is not None:
            return (game, self.min_score+depth)
        elif depth > self.max_depth:
            return (game,  beta if is_my_turn else alpha)
        else:
            possible_moves = game.get_possible_next_states()
            results = []
            for state in possible_moves:
                game_clone = copy.deepcopy(game)
                game_clone.debug = False
                game_clone.move(state)
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
