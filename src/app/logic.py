from src.app.board import Board


class Logic:
    MIN_VALUE = -999
    MAX_VALUE = 999
    EMPTY = ' '
    O_SYMBOL = 'O'
    X_SYMBOL = 'X'

    def __init__(self):
        self.board = Board()

    def determine_best_score_and_move(self, board, depth, is_maximizing, symbol):
        winner = self.board.check_win(board, symbol)
        if winner and symbol == Logic.X_SYMBOL:
            return {'score': Logic.MIN_VALUE, 'index': None}
        elif winner and symbol == Logic.O_SYMBOL:
            return {'score': Logic.MAX_VALUE, 'index': None}
        elif self.board.is_board_full(board):
            return {'score': 0, 'index': None}

        if is_maximizing:
            symbol = Logic.O_SYMBOL
            comparison_function = max
            initial_best_score = Logic.MIN_VALUE
        else:
            symbol = Logic.X_SYMBOL
            comparison_function = min
            initial_best_score = Logic.MAX_VALUE

        return self.calculate_score(board, depth, symbol, initial_best_score, comparison_function)

    def calculate_score(self, board, depth, symbol, initial_best_score, comparison_function):
        best_score = initial_best_score
        move_index = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == Logic.EMPTY:
                    board[i][j] = symbol
                    if symbol == 'O':
                        new_symbol = Logic.X_SYMBOL
                        is_maximizing = False
                    else:
                        new_symbol = Logic.O_SYMBOL
                        is_maximizing = True
                    result = self.determine_best_score_and_move(board, depth + 1, is_maximizing, new_symbol)
                    board[i][j] = Logic.EMPTY
                    if comparison_function(result['score'], best_score) == result['score']:
                        best_score = result['score']
                        move_index = (i, j)
        return {'score': best_score, 'index': move_index}
