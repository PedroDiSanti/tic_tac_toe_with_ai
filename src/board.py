"""
Represents a tic-tac-toe board.
"""


class Board:
    """Initializes the board with empty cells."""
    def __init__(self):
        """
        Initializes the board with empty cells.

        :param self: object instance
        :type self: object
        """
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    @staticmethod
    def print_board(board: list):
        """
        Prints the given board.

        :param board: A list representing the board.
        :type board: list
        """
        for row in board:
            print(row)

    @staticmethod
    def is_board_full(board: list) -> bool:
        """
        Check if the given board is full.

        :param board: The game board represented as a 2D list.
        :return: True if the board is full, False otherwise.
        """
        for row in board:
            if ' ' in row:
                return False
        return True

    def check_win(self, board: list, player: str) -> bool:
        """
        Check if the given player has won the game based on the current state of the board.

        :param board: A 2D list representing the current state of the tic-tac-toe board.
        :param player: The player to check for a win, represented by string 'X' or 'O'.
        :return: True if the player has won the game, False otherwise.
        """
        win_conditions = [
            self._check_columns(board, player),  # columns
            self._check_rows(board, player),  # rows
            self._check_main_diagonal(board, player),  # main diag
            self._check_sub_diagonal(board, player)  # second diag
        ]
        return any(any(row) for row in win_conditions)

    @staticmethod
    def _check_main_diagonal(board: list, player: str) -> list:
        """
        Check if the main diagonal of the board contains all the same player's marks.

        :param board: A 2-dimensional list representing the game board.
        :param player: A string representing the player's mark ('X' or 'O').
        :return: A list containing a boolean value indicating whether the main diagonal contains
                    all the same marks.
        """
        return [board[0][0] == player and board[1][1] == player and board[2][2] == player]

    @staticmethod
    def _check_sub_diagonal(board: list, player: str) -> list:
        """
        :param board: The game board represented as a 2-dimensional list.
        :param player: The player to check for in the sub-diagonal.
        :return: A list containing a boolean value indicating whether the player has won in
                    the sub-diagonal.
        """
        return [board[0][2] == player and board[1][1] == player and board[2][0] == player]

    @staticmethod
    def _check_rows(board: list, player: str) -> list:
        """
        Check if any row on the board contains all the cells filled by the specified player.

        :param board: A 2D list representing the game board. Each element in the list represents
                        a cell on the board.
                      The cell can be empty or filled by a player ('X' or 'O').
        :param player: A string representing the player to check for. Valid values are 'X' or 'O'.
        :return: A list of boolean values indicating whether each row on the board contains cells
                    filled by the specified player.
                 True represents a row with all cells filled by the player, False otherwise.
        """
        return [board[i][0] == player and board[i][1] == player and board[i][2] == player for i in
                range(3)]

    @staticmethod
    def _check_columns(board: list, player: str) -> list:
        """
        Check columns for a win.

        :param board: The game board represented as a 2-dimensional list.
        :param player: The player to check for a win.
        :return: A list of boolean values where each value represents whether the player has won in
                    the corresponding column.

        Algorithm:
        1. Iterate over the column indices of the board.
        2. Check if the player has placed their mark in all three positions of the column.
        3. Append the result to the list.
        4. Return the list of column win results.
        """
        return [board[0][j] == player and board[1][j] == player and board[2][j] == player for j in
                range(3)]
