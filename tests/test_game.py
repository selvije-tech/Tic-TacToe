import sys
import os
import unittest
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from game import TicTacToeGame, Move

class TestTicTacToeGame(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToeGame()

    def test_initial_state(self):
        self.assertFalse(self.game.has_winner())
        self.assertFalse(self.game.is_tied())

    def test_valid_move(self):
        move = Move(0, 0, "X")
        self.assertTrue(self.game.is_valid_move(move))
        self.game.process_move(move)
        self.assertFalse(self.game.is_valid_move(move))

    def test_winner(self):
        moves = [
            Move(0, 0, "X"), Move(1, 0, "O"),
            Move(0, 1, "X"), Move(1, 1, "O"),
            Move(0, 2, "X")
        ]
        for move in moves:
            self.game.process_move(move)
            self.game.toggle_player()
        self.assertTrue(self.game.has_winner())
        self.assertEqual(self.game.winner_combo, [(0, 0), (0, 1), (0, 2)])

    def test_tied_game(self):
        moves = [
            Move(0, 0, "X"), Move(0, 1, "O"), Move(0, 2, "X"),
            Move(1, 0, "X"), Move(1, 1, "X"), Move(1, 2, "O"),
            Move(2, 0, "O"), Move(2, 1, "X"), Move(2, 2, "O")
        ]
        for move in moves:
            self.game.process_move(move)
            self.game.toggle_player()
        self.assertFalse(self.game.has_winner())
        self.assertTrue(self.game.is_tied())

if __name__ == "__main__":
    pytest.main()
