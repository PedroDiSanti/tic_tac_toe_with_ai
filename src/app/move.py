import random

from src.app.logic import Logic


class Move:
    """
    The Move class represents a move in a game.

    Attributes:
    symbol (str): The character that represents the move on the game board.

    Methods:
    __init__(self, symbol: str)
    is_valid_move(i: int, j: int, board: list) -> bool
    get_move(self, board: list, symbol: str) -> tuple
    _generate_player_move(self, board)
    _generate_auto_move(self, board, valid_moves)
    """

    def __init__(self, symbol):
        """
        The constructor for the AutoPlay class.

        Args:
        symbol (str): The character that will represent the computer's positions on the board.
        """
        self.symbol = symbol
        self.logic = Logic()
        self.depth = 0

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
        if symbol == "O":
            move = self._generate_auto_move(board)
        else:
            move = self._generate_player_move(board)

        print(f"({symbol}) move: {move}")
        return move

    def _generate_player_move(self, board: list) -> list:
        """
        :param board: A list representing the current state of the game board.
        :return: A list containing the row and column indices of the player's move.

        This method is used to generate a move for the player with marker 'X'. It prompts the player to enter their move in the format (row, col). The input is split into row and column indices
        *, converted to integers using the map function, and assigned to variables i and j respectively. It then checks if the move is valid using the is_valid_move method. If the move is valid
        *, it returns a list containing the row and column indices of the player's move.
        """
        while True:
            print("It's X turn. Enter your move in the format (row, col):")
            move = input()
            i, j = map(int, move.split(','))
            if self.is_valid_move(i, j, board):
                return [i, j]

    def _generate_auto_move(self, board: list) -> list:
        """
        :param board: The current state of the game board.
        :param valid_moves: A list of valid moves.
        :return: The chosen move as a tuple (row, column).

        This method is responsible for generating an automatic move for the game. It iterates through each cell of the game board and checks if it is a valid move using the `is_valid_move` method
        *. If a cell is a valid move, it adds it to the `valid_moves` list. Finally, it selects a random move from the `valid_moves` list and returns it as the chosen move.

        Example usage:
            board = [['X', 'O', ''],
                     ['', 'X', 'O'],
                     ['', '', '']]
            valid_moves = []
            game._generate_auto_move(board, valid_moves)
            # Returns a random valid move (e.g., (0, 2))
        """
        move = self.logic.determine_best_score_and_move(board, self.depth, True, 'O')
        i, j = move.get("index")[0], move.get("index")[1]
        return [i, j]
