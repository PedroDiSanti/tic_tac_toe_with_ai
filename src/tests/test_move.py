import unittest
from unittest.mock import patch

from src.app.move import Move


class TestMoves(unittest.TestCase):
    def setUp(self):
        self.player = Move('X')
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
        valid_moves = [(0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        self.assertIn(move, valid_moves)

    @patch('builtins.input', return_value='0,2')
    def test_get_move_player(self, mock_input):
        move = self.player.get_move(self.board, 'X')
        self.assertEqual(move, [0, 2])

    @patch('builtins.input', return_value='0,1')
    def test_generate_player_move(self, mock_input):
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(self.player._generate_player_move(board), [0, 1])

    @patch('src.app.move.Moves._generate_auto_move', return_value=(1, 1))
    def test_get_move_auto(self, mock_auto_move):
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(self.player.get_move(board, 'O'), (1, 1))
