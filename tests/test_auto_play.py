import unittest
from app.auto_play import ComputerPlayer


class TestComputerPlayer(unittest.TestCase):
    def setUp(self):
        self.player = ComputerPlayer('X')
        self.board = [
            ['X', 'O', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    def test_is_valid_move(self):
        # Test when move inside the board and spot is vacant
        self.assertTrue(self.player.is_valid_move(1, 1, self.board))

        # Test when spot is occupied
        self.assertFalse(self.player.is_valid_move(0, 0, self.board))

        # Test when move is outside the board
        self.assertFalse(self.player.is_valid_move(-1, 2, self.board))
        self.assertFalse(self.player.is_valid_move(1, 3, self.board))

    def test_get_move(self):
        move = self.player.get_move(self.board, 'O')
        valid_moves = [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        self.assertIn(move, valid_moves)