import builtins

from src.board import Board


class Logic:
    """
    A class representing the logic of a game using the Minimax algorithm.

    Attributes:
        MIN_VALUE (int): Minimum value for score.
        MAX_VALUE (int): Maximum value for score.
        EMPTY (str): Symbol representing an empty space on the game board.
        O_SYMBOL (str): Symbol representing the player O.
        X_SYMBOL (str): Symbol representing the player X.

    Methods:
        __init__(): Initializes the Logic object.
        determine_best_score_and_move(board, depth, is_maximizing, symbol): Determines the best score and move for the given board and symbol.
        calculate_score(board, depth, symbol, initial_best_score, comparison_function): Calculates the score for the given board and symbol.

    """
    MIN_VALUE = -999
    MAX_VALUE = 999
    EMPTY = ' '
    O_SYMBOL = 'O'
    X_SYMBOL = 'X'

    def __init__(self):
        """
        Initializes a new instance of the class.

        :param self: The object being initialized.
        """
        self.board = Board()

    def determine_best_score_and_move(self, board: list, depth: int, is_maximizing: True, symbol: str) -> dict:
        """
        :param board: the current state of the tic-tac-toe board (2D list)
        :param depth: the depth of the current move in the game tree (integer)
        :param is_maximizing: indicates if the current move is maximizing or minimizing (boolean)
        :param symbol: the symbol (X or O) of the current player (string)
        :return: a dictionary containing the best score and move index {'score': score, 'index': move_index}

        The determine_best_score_and_move method takes in the current state of the tic-tac-toe board, the depth of the move,
        whether the move is maximizing or minimizing, and the symbol of the current player. It returns the best score and move index
        for the current player.

        First, it checks if there is a winner on the current board for the current player's symbol. If there is a winner and the
        current player's symbol is X, it returns a dictionary with a score of Logic.MIN_VALUE and a None move index. If there is a
        winner and the current player's symbol is O, it returns a dictionary with a score of Logic.MAX_VALUE and a None move index.
        If the board is full, it returns a dictionary with a score of 0 and a None move index.

        If it is a maximizing move, it sets the symbol to O, the comparison function to max, and the initial best score to
        Logic.MIN_VALUE. Otherwise, it sets the symbol to X, the comparison function to min, and the initial best score to
        Logic.MAX_VALUE.

        Finally, it calls the calculate_score method to calculate the best score and move index for the current player using the
        provided parameters.
        """
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

    def calculate_score(self, board: list, depth: int, symbol: str, initial_best_score: int,
                        comparison_function: builtins) -> dict:
        """
        Calculate the best score and move index for the given board.

        :param board: A 2D list representing the Tic-Tac-Toe board.
        :param depth: The depth of the current search algorithm.
        :param symbol: The symbol of the current player.
        :param initial_best_score: The initial best score. Used for comparison.
        :param comparison_function: A comparison function used to compare scores.
        :return: A dictionary containing the best score and move index.

        """
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
