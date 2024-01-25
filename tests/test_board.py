import io
import ast
import unittest
from unittest.mock import patch

from src.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_state(self):
        self.assertEqual(self.board.board, [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_board(self, mock_stdout):
        self.board.print_board(self.board.board)
        output = [ast.literal_eval(item) for item in mock_stdout.getvalue().splitlines()]
        self.assertEqual(self.board.board, output)
