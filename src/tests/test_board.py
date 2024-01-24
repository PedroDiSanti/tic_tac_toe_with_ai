import io
import ast
import unittest
from unittest.mock import patch

from src.app.board import Board  # Assume this is your module


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_state(self):
        """
        This method is used to test the initial state of the board in a Tic-Tac-Toe game.

        :return: None
        """
        self.assertEqual(self.board.board, [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_board(self, mock_stdout):
        """
        :param mock_stdout: A mock object representing the standard output (stdout)
        :return: None

        This method is a unit test for the `print_board` method of a board object. It verifies that the `print_board` method correctly outputs the contents of the board to the standard output
        *.

        The `mock_stdout` parameter is a mock object that mocks the stdout stream. It is used to capture the output of the `print_board` method.

        The method performs the following steps:
        1. Calls the `print_board` method of the board object being tested.
        2. Captures the output from the stdout stream using the `mock_stdout.getvalue()` method.
        3. Splits the captured output into lines using the `splitlines()` method.
        4. Parses each line as a literal using the `ast.literal_eval()` method to obtain the printed board contents.
        5. Asserts that the board contents obtained from `self.board.board` are equal to the parsed output.

        This method is intended to be used as a unit test case in a test suite for the board object.
        """
        self.board.print_board()
        output = [ast.literal_eval(item) for item in mock_stdout.getvalue().splitlines()]
        self.assertEqual(self.board.board, output)
