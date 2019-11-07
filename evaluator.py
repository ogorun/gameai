
class Evaluator:

    def evaluate(self, game):
        result = game.evaluate()
        if result is not None:
            return result

        return 0
