import unittest
from unittest.mock import patch, Mock
from src.app.game import Game
from src.app.board import Board
from src.app.move import Move


class TestGame(unittest.TestCase):
    def setUp(self):
        self.mock_board = Mock(spec=Board)
        self.mock_player1 = Mock(spec=Move)
        self.mock_player2 = Mock(spec=Move)
        self.game = Game(self.mock_player1, self.mock_player2, self.mock_board)

    def test_check_win_condition_true(self):
        self.mock_board.board = [
            ['X', 'X', 'X'],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.assertTrue(self.game.check_win('X'))

    def test_check_win_condition_false(self):
        self.mock_board.board = [
            ['X', ' ', ' '],
            [' ', 'X', ' '],
            [' ', ' ', ' ']
        ]
        self.assertFalse(self.game.check_win('X'))

    @patch('src.app.game.Game.check_win', return_value=True)
    def test_game_win(self, mock_check_win):
        self.mock_board.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.mock_player1.get_move.return_value = [0, 0]
        self.mock_player1.symbol = "X"
        self.game.start()
        mock_check_win.assert_called_once()
