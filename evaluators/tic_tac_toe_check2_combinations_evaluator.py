from evaluator import Evaluator

class TicTacToeCheck2CombinationsEvaluator(Evaluator):

    def evaluate(self, game):
        lines = game.count_lines(game.state)
        if lines[3][game.labels[0]] > 0:
            return 100
        if lines[3][game.labels[1]] > 0:
            return -100

        if game.is_first_agent_turn and lines[2][game.labels[0]] > 0:
            return 50
        if not game.is_first_agent_turn and lines[2][game.labels[1]] > 0:
            return -50

        if lines[2][game.labels[0]] > 1:
            return 30
        if lines[2][game.labels[1]] > 1:
            return -30

        if lines[2][game.labels[0]] > 0:
            return 10
        if lines[2][game.labels[1]] > 0:
            return -10

        return 0
