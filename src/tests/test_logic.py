import unittest
from src.app.logic import Logic


class TestLogic(unittest.TestCase):
    def setUp(self):
        self.logic = Logic()
        self.test_board = [[Logic.EMPTY] * 3 for _ in range(3)]

    def test_determine_best_score_and_move_min_value(self):
        self.test_board[0][0] = Logic.X_SYMBOL
        self.test_board[0][1] = Logic.X_SYMBOL
        self.test_board[0][2] = Logic.X_SYMBOL
        result = self.logic.determine_best_score_and_move(self.test_board, 1, False, Logic.X_SYMBOL)
        self.assertEqual(result, {'score': Logic.MIN_VALUE, 'index': None})

    def test_determine_best_score_and_move_max_value(self):
        self.test_board[0][0] = Logic.O_SYMBOL
        self.test_board[0][1] = Logic.O_SYMBOL
        self.test_board[0][2] = Logic.O_SYMBOL
        result = self.logic.determine_best_score_and_move(self.test_board, 1, True, Logic.O_SYMBOL)
        self.assertEqual(result, {'score': Logic.MAX_VALUE, 'index': None})

    def test_determine_best_score_and_move_full_board(self):
        self.test_board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['X', 'O', 'O']
        ]
        result = self.logic.determine_best_score_and_move(self.test_board, 1, True, Logic.O_SYMBOL)
        self.assertEqual(result, {'score': 0, 'index': None})
