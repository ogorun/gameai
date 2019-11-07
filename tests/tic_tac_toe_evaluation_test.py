import unittest
from games.tictactoe import TicTacToe
from evaluators.tic_tac_toe_check2_combinations_evaluator import TicTacToeCheck2CombinationsEvaluator

class TicTacToeHeuristicEvaluationTest(unittest.TestCase):
    evaluator = TicTacToeCheck2CombinationsEvaluator()

    def test_three(self):
        game = TicTacToe(['X','X','X','O','O',5,6,7,8])
        self.assertEqual(self.evaluator.evaluate(game), 'X', "Should be X")

    def test_next_three(self):
        game = TicTacToe(['X',1,2,'O','O',5,'X',7,8])
        self.assertEqual(self.evaluator.evaluate(game), -100, "Should be -100")

    def test_two_plus_next_three(self):
        game = TicTacToe(['X','X',2,'O','O',5,6,7,8])
        self.assertEqual(self.evaluator.evaluate(game), -100, "Should be -100")

    def test_fork(self):
        game = TicTacToe(['X',1,'X',3,'O',5,'O',7,'X'])
        self.assertEqual(self.evaluator.evaluate(game), 50, "Should be 50")

    def test_next_fork(self):
        game = TicTacToe([0,'X',2,'X','O',5,6,'O',8])
        self.assertEqual(self.evaluator.evaluate(game), -50, "Should be -50")

    def test_fork_plus_next_three(self):
        game = TicTacToe(['X',1,'X',3,'O',5,6,'O','X'])
        self.assertEqual(self.evaluator.evaluate(game), -100, "Should be -100")

    def test_two(self):
        game = TicTacToe(['X',1,2,'X','O',5,6,7,8])
        self.assertEqual(self.evaluator.evaluate(game), 20, "Should be 20")

    # def test_two_blocked_by_possible_next_fork(self):
    #     game = TicTacToe(['O',1,2,3,'X',5,'X',7,'O'])
    #     self.assertEqual(self.evaluator.evaluate(game), -50, "Should be -50")

    def test_two_with_not_realisable_next_fork(self):
        game = TicTacToe(['O',1,2,3,'X',5,6,'X','O'])
        self.assertEqual(self.evaluator.evaluate(game), 20, "Should be 20")

    def test_next_two(self):
        game = TicTacToe(['X','O',2,3,4,5,6,7,8])
        self.assertEqual(self.evaluator.evaluate(game), -20, "Should be -20")

    def test_one_only(self):
        game = TicTacToe(['X','O',2,'O','X','X','O','X','O'])
        self.assertEqual(self.evaluator.evaluate(game), 0, "Should be 0")


if __name__ == '__main__':
    unittest.main()