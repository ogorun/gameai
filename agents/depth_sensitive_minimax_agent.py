from agent import Agent
from game import Game


class DepthSensitiveMinimaxAgent(Agent):

    def move(self, game: Game, possible_steps=None):
        result = self.__minimax(game, 0, possible_steps=possible_steps)
        return result[0]

    def __minimax(self, game: Game, depth, is_my_turn=True, step=None, possible_steps=None):
        winner = game.evaluate()
        if winner == self.label:
            return (step, 10-depth)
        elif winner == 'draw':
            return (step, 0)
        elif winner is not None:
            return (step, -10+depth)
        else:
            if possible_steps is None:
                possible_steps = game.get_possible_next_steps()
            results = []
            for current_step in possible_steps:
                game_clone = game.copy_and_move(current_step)
                result = self.__minimax(game_clone, depth + 1, not is_my_turn, current_step)
                results.append((current_step, result[1]))

            if is_my_turn:
                final = max(results, key=lambda item: item[1])
            else:
                final = min(results, key=lambda item: item[1])
            return final
