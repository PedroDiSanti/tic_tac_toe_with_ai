import io
import unittest
from unittest.mock import patch
from app.tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_initial_state(self):
        initial_board = [[' ' for _ in range(3)] for _ in range(3)]
        self.assertEqual(self.game.board, initial_board)
        self.assertEqual(self.game.current_player, 'X')

    @patch('builtins.input', return_value='0,0')
    def test_valid_move_updates_the_board(self, mock_input):
        self.game.start()
        self.assertEqual(self.game.board[0][0], 'X')

    def test_winning_conditions(self):
        self.game.board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(self.game.check_win('X'))

    @patch('builtins.input', return_value='3,3')
    def test_invalid_move_does_not_update_the_board(self, mock_input):
        initial_board_state = self.game.board.copy()
        self.game.start()
        self.assertEqual(self.game.board, initial_board_state)

    def test_player_switches_after_move(self):
        initial_player = self.game.current_player
        self.game.change_player()
        self.assertNotEqual(initial_player, self.game.current_player)

    def test_is_valid_move(self):
        self.assertTrue(self.game.is_valid_move(0, 0))
        self.assertFalse(self.game.is_valid_move(3, 3))
        self.assertFalse(self.game.is_valid_move(-1, -1))

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='0,2')
    def test_winner(self, mock_input, mock_stdout):
        self.game.board = [['X', 'X', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.game.start()
        output = mock_stdout.getvalue().splitlines()
        self.assertEqual(output[7], "X Wins!")


