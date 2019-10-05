from game import Game
from games.tictactoe import TicTacToe
from agent import Agent
import copy


class MinimaxAgent(Agent):

    def __init__(self, label):
        super().__init__(label)

    def move(self, game: Game):
        result = self.__minimax(game)
        return result[0].state

    def __minimax(self, game: Game, is_my_turn=True):
        winner = game.evaluate()
        if winner == self.label:
            return (game, 10)
        elif winner == 'draw':
            return (game, 0)
        elif winner is not None:
            return (game, -10)
        else:
            possible_moves = game.get_possible_next_states()
            results = []
            for state in possible_moves:
                game_clone = copy.deepcopy(game)
                game_clone.set_debug(False)
                game_clone.move(state)
                result = self.__minimax(game_clone, not is_my_turn)
                results.append((game_clone, result[1]))

            if is_my_turn:
                final = max(results, key=lambda item: item[1])
            else:
                final = min(results, key=lambda item: item[1])
            return final



