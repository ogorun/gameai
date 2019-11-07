from agent import Agent
from game import Game


class MinimaxWithAlphaBeta(Agent):

    def __init__(self, label, max_depth=10):
        super().__init__(label)
        self.max_depth = max_depth
        self.min_score = -1000000
        self.max_score = 1000000

    def move(self, game: Game, possible_steps=None):
        result = self.__minimax(game, 0, self.min_score, self.max_score, possible_steps=possible_steps)
        return result[0]

    def __minimax(self, game: Game, depth, alpha, beta, is_my_turn=True, step=None, possible_steps=None):

        winner = game.evaluate()
        if winner == self.label:
            return (step, self.max_score-depth)
        elif winner == 'draw':
            return (step, 0)
        elif winner is not None:
            return (step, self.min_score+depth)
        elif depth >= self.max_depth:
            my_label_index = [index for index in [0,1] if game.labels[index] == self.label][0]
            factor = (1 if my_label_index == 0 else -1)
            score = self.evaluator.evaluate(game)*factor
            if score > 0:
                score = score - depth
            elif score < 0:
                score = score + depth
            return (step, score)
        else:
            if possible_steps is None:
                possible_steps = game.get_possible_next_steps()
            results = []
            for current_step in possible_steps:
                game_clone = game.copy_and_move(current_step)
                result = self.__minimax(game_clone, depth + 1, alpha, beta, not is_my_turn, current_step)
                results.append((current_step, result[1]))

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
