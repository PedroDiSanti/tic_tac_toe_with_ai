class Board:
    """
    Represents a tic-tac-toe board.
    """

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

    @staticmethod
    def check_win(board: list, player: str) -> bool:
        """
        Check if the given player has won the game based on the current state of the board.

        :param board: A 2D list representing the current state of the tic-tac-toe board.
        :param player: The player to check for a win, represented by string 'X' or 'O'.
        :return: True if the player has won the game, False otherwise.
        """
        win_conditions = [
            [board[0][j] == player and board[1][j] == player and board[2][j] == player for j in range(3)],  # columns
            [board[i][0] == player and board[i][1] == player and board[i][2] == player for i in range(3)],  # rows
            [board[0][0] == player and board[1][1] == player and board[2][2] == player],  # main diag
            [board[0][2] == player and board[1][1] == player and board[2][0] == player]  # second diag
        ]
        return any(any(row) for row in win_conditions)
