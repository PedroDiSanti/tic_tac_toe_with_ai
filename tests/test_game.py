import io
import unittest
from unittest.mock import patch

from src.game import Game  # Replace with your actual module name.


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    @patch('src.move.Move.get_move', return_value=(1, 1))
    @patch('src.board.Board.check_win', return_value=True)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_start(self, mock_stdout, mock_check_win, mock_get_move):
        """Test the game start method."""
        result = self.game.start()
        value = mock_stdout.getvalue().splitlines()
        self.assertIsNotNone(value)
        self.assertIn(value[6], ['X Wins!', 'O Wins!'])
