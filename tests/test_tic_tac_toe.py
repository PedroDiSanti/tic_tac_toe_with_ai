import io
import unittest
from unittest.mock import patch

from app.auto_play import ComputerPlayer
from app.tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe(ComputerPlayer('X'), ComputerPlayer('O'))

    def test_initial_state(self):
        expected_board = [[' ' for _ in range(3)] for _ in range(3)]
        self.assertEqual(self.game.board, expected_board)
        self.assertEqual(self.game.players[0].symbol, 'X')
        self.assertEqual(self.game.players[1].symbol, 'O')

    def test_check_win(self):
        # No win yet
        self.assertFalse(self.game.check_win('X'))

        # Horizontal win
        self.game.board[0] = ['X', 'X', 'X']
        self.assertTrue(self.game.check_win('X'))

        # Vertical win
        self.game.board = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        self.assertTrue(self.game.check_win('X'))

        # Diagonal win
        self.game.board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertTrue(self.game.check_win('X'))

    def test_winning_conditions(self):
        self.game.board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(self.game.check_win('X'))

    @patch('builtins.input', return_value='3,3')
    def test_invalid_move_does_not_update_the_board(self, mock_input):
        initial_board_state = self.game.board.copy()
        self.game.start()
        self.assertEqual(self.game.board, initial_board_state)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='0,2')
    def test_winner(self, mock_input, mock_stdout):
        self.game.start()
        output = mock_stdout.getvalue().splitlines()
        self.assertIn(output[len(output) - 1], ["X Wins!", "O Wins!"])
