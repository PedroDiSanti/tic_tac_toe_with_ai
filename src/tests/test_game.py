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
        """
        Test method for checking win condition when it is true.

        :return: None
        """
        self.mock_board.board = [
            ['X', 'X', 'X'],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.assertTrue(self.game.check_win('X'))

    def test_check_win_condition_false(self):
        """
        Test case for checking the win condition is false.

        :return: None
        """
        self.mock_board.board = [
            ['X', ' ', ' '],
            [' ', 'X', ' '],
            [' ', ' ', ' ']
        ]
        self.assertFalse(self.game.check_win('X'))

    @patch('src.app.game.Game.check_win', return_value=True)
    def test_game_win(self, mock_check_win):
        """
        :param mock_check_win: A patched version of the 'check_win' method from the 'Game' class. This is used to mock the behavior of the 'check_win' method during testing.
        :return: None

        This method is a unit test for the 'game_win' method of a game. It tests whether the 'game_win' method is called during the execution of the 'start' method of the game.

        The test sets up the following conditions:
        - The 'board' attribute of the 'mock_board' object is set to a 3x3 grid of empty spaces.
        - The 'get_move' method of the 'mock_player1' object is set to return the coordinates [0, 0].
        - The 'symbol' attribute of the 'mock_player1' object is set to "X".

        The 'start' method of the game is then called, which triggers the execution of the 'game_win' method. Finally, the test asserts that the 'check_win' method is called exactly once.

        This test case is used to verify that the 'game_win' method is called correctly and behaves as expected when all the relevant conditions are met.
        """
        self.mock_board.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.mock_player1.get_move.return_value = [0, 0]
        self.mock_player1.symbol = "X"
        self.game.start()
        mock_check_win.assert_called_once()
