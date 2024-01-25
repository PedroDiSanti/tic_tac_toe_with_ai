import unittest
from unittest.mock import patch
from io import StringIO

from src.move import Move


class TestMove(unittest.TestCase):
    def setUp(self):
        self.move = Move()
        self.board = [['X', 'O', ' '],
                      [' ', 'X', 'O'],
                      [' ', ' ', ' ']]

    def test_is_valid_move(self):
        self.assertFalse(self.move.is_valid_move(1, 1, self.board))
        self.assertTrue(self.move.is_valid_move(0, 2, self.board))
        self.assertFalse(self.move.is_valid_move(3, 3, self.board))

    @patch('sys.stdin', new_callable=StringIO)
    def test_generate_player_move(self, mock_input):
        mock_input.write('0,2\n')
        mock_input.seek(0)
        expected_result = [0, 2]
        self.assertEqual(self.move._generate_player_move(self.board), expected_result)

    def test_generate_auto_move(self):
        auto_move = self.move._generate_auto_move(self.board)
        valid_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
        self.assertIn(tuple(auto_move), valid_moves)

    @patch('src.move.Move._generate_auto_move', return_value=(1, 1))
    def test_get_move_auto(self, mock_auto_move):
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(self.move.get_move(board, 'O'), (1, 1))

    @patch('src.move.Move._generate_player_move', return_value=(1, 1))
    def test_get_move_player(self, mock_player_move):
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(self.move.get_move(board, 'X'), (1, 1))
