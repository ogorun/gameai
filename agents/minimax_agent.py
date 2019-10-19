from game import Game
from agent import Agent


class MinimaxAgent(Agent):

    def move(self, game: Game, possible_states=None):
        result = self.__minimax(game, possible_states=possible_states)
        return result[0].state

    def __minimax(self, game: Game, is_my_turn=True, possible_states=None):
        winner = game.evaluate()
        if winner == self.label:
            return (game, 10)
        elif winner == 'draw':
            return (game, 0)
        elif winner is not None:
            return (game, -10)
        else:
            if possible_states is None:
                possible_states = game.get_possible_next_states()
            results = []
            for state in possible_states:
                game_clone = game.next_state_clone(state)
                result = self.__minimax(game_clone, not is_my_turn)
                results.append((game_clone, result[1]))

            if is_my_turn:
                final = max(results, key=lambda item: item[1])
            else:
                final = min(results, key=lambda item: item[1])
            return final



