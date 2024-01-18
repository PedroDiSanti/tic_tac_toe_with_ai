import random


class AutoPlay:
    """
    A class that represents the computer's automated movements within a Tic Tac Toe game.

    Attributes:
    symbol (str): The symbol representing the computer in the game.

    Methods:
    is_valid_move(i: int, j: int, board): Checks if the identified move is valid.
    get_move(board, symbol): Determines and returns the computer's next move.
    """

    def __init__(self, symbol):
        """
        The constructor for the AutoPlay class.

        Args:
        symbol (str): The character that will represent the computer's positions on the board.
        """
        self.symbol = symbol

    @staticmethod
    def is_valid_move(i: int, j: int, board: list) -> bool:
        """
        Checks if the identified move (i, j) is valid on the provided game board.

        Args:
        i (int): The row of the move.
        j (int): The column of the move.
        board (list of str): The current state of the game board.

        Returns:
        bool: True if the move is valid, False otherwise.
        """
        if i < 0 or i >= 3 or j < 0 or j >= 3:  # check if the move is within the board
            return False
        if board[i][j] != ' ':  # check if the position is not occupied
            return False
        return True

    def get_move(self, board: list, symbol: str):
        """
        Determines and returns the computer's next move.

        Args:
        board (list of str): The current state of the game board.
        symbol (str): The character that will represent the computer's positions on the board.

        Returns:
        tuple: The computer's chosen move as a tuple of row index and column index.
        """
        valid_moves = []
        for i in range(3):
            for j in range(3):
                if self.is_valid_move(i, j, board):
                    valid_moves.append((i, j))

        move = random.choice(valid_moves)
        print(f"Computer ({symbol}) move: {move}")
        return move
