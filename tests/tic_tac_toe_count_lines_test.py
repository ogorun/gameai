import unittest
from games.tictactoe import TicTacToe

class TicTacToeCountLinesTest(unittest.TestCase):

    def test_1(self):
        game = TicTacToe(['O',1,2,3,4,5,6,7,8])
        self.assertEqual( {3: {'X': 0, 'O': 0}, 2: {'X':0, 'O': 0}}, game.count_lines(game.state))

    def test_2(self):
        game = TicTacToe(['O','X','O',3,4,5,6,7,8])
        self.assertEqual( {3: {'X': 0, 'O': 0}, 2: {'X':0, 'O': 0}}, game.count_lines(game.state))

    def test_3(self):
        game = TicTacToe(['O',1,2,'O','X',5,6,7,8])
        self.assertEqual( {3: {'X': 0, 'O': 0}, 2: {'X':0, 'O': 1}}, game.count_lines(game.state))

    def test_4(self):
        game = TicTacToe(['X','X','O','O','O','X','X','O','X'])
        self.assertEqual( {3: {'X': 0, 'O': 0}, 2: {'X':0, 'O': 0}}, game.count_lines(game.state))

    def test_5(self):
        game = TicTacToe(['X','X','X','O','O','X','X','O','O'])
        self.assertEqual( {3: {'X': 1, 'O': 0}, 2: {'X':0, 'O': 0}}, game.count_lines(game.state))

    def test_6(self):
        game = TicTacToe(['X','X','X','O','O',5,6,7,8])
        self.assertEqual( {3: {'X': 1, 'O': 0}, 2: {'X':0, 'O': 1}}, game.count_lines(game.state))

    def test_7(self):
        game = TicTacToe(['X','X',2,'O','O',5,6,7,8])
        self.assertEqual( {3: {'X': 0, 'O': 0}, 2: {'X':1, 'O': 1}}, game.count_lines(game.state))

    def test_8(self):
        game = TicTacToe(['X',1,'X',3,'O',5,6,'O','X'])
        self.assertEqual( {3: {'X': 0, 'O': 0}, 2: {'X':2, 'O': 1}}, game.count_lines(game.state))

    def test_9(self):
        game = TicTacToe(['X',1,'X',3,'O',5,'O',7,'X'])
        self.assertEqual( {3: {'X': 0, 'O': 0}, 2: {'X':2, 'O': 0}}, game.count_lines(game.state))

    def test_10(self):
        game = TicTacToe(['O',1,2,3,'X',5,6,'X','O'])
        self.assertEqual( {3: {'X': 0, 'O': 0}, 2: {'X':1, 'O': 0}}, game.count_lines(game.state))

    def test_11(self):
        game = TicTacToe(['O',1,2,3,'X',5,'X',7,'O'])
        self.assertEqual( {3: {'X': 0, 'O': 0}, 2: {'X':1, 'O': 0}}, game.count_lines(game.state))
