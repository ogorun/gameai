from evaluator import Evaluator


class SplitStacksNimEvaluator(Evaluator):

    def evaluate(self, game):
        evens = [stack for stack in game.state if stack % 2 == 0]
        is_odd_number_of_evens = (len(evens) % 2 == 1)
        return (int(is_odd_number_of_evens)*2 - 1)*(-1**game.is_first_agent_turn)
