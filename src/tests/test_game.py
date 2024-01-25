import unittest
from unittest.mock import Mock, patch

from src.app.board import Board
from src.app.game import Game
from src.app.move import Move


class TestGame(unittest.TestCase):
    def setUp(self):
        self.user_player = Move('X')
        self.computer_player = Move('O')
        self.board = Board()
        self.game = Game(self.user_player, self.computer_player, self.board)

    @patch("builtins.print")
    def test_start(self, mock_print):
        """ Test the start of the game. """
        # Mocking get_move function to return set values for testing
        self.user_player.get_move = Mock(return_value=(0, 0))
        self.computer_player.get_move = Mock(return_value=(1, 1))

        # Mocking check_win function to return False initially and then True on subsequent call
        self.board.check_win = Mock(side_effect=[False, True])

        # start the game
        self.game.start()

        # Check if print statement is called with the winning message
        mock_print.assert_called_with(f"{self.computer_player.symbol} Wins!")

        # Check if symbols are placed correctly
        self.assertEqual(self.board.board[0][0], self.user_player.symbol)
        self.assertEqual(self.board.board[1][1], self.computer_player.symbol)