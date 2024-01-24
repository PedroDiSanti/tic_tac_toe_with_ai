import io
import ast
import unittest
from unittest.mock import patch

from src.app.board import Board  # Assume this is your module


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_state(self):
        """Test the board's initial state"""
        self.assertEqual(self.board.board, [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_board(self, mock_stdout):
        """Test the board's print function"""
        self.board.print_board()
        output = [ast.literal_eval(item) for item in mock_stdout.getvalue().splitlines()]
        self.assertEqual(self.board.board, output)