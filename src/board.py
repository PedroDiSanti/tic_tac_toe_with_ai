class Board:
    """
    Board
    =====

    A class representing the game board.

    Methods
    -------

    __init__()
        Constructor method which initializes the game board with empty spaces.

    print_board()
        Prints the current state of the game board to the console.
    """

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    @staticmethod
    def print_board(board):
        """Prints the current state of the game board to the console."""
        for row in board:
            print(row)

    @staticmethod
    def is_board_full(board):
        """
        Check if the game board is full.

        :return: True if the board is full, False otherwise.
        """
        for row in board:
            if ' ' in row:
                return False
        return True

    @staticmethod
    def check_win(board, player: str):
        """
        Checks if the specified player has won the game.

        Args:
        player (str): The symbol of the player to check for a win.

        Returns:
        bool: True if the player has won, False otherwise.
        """
        win_conditions = [
            [board[0][j] == player and board[1][j] == player and board[2][j] == player for j in range(3)],  # columns
            [board[i][0] == player and board[i][1] == player and board[i][2] == player for i in range(3)],  # rows
            [board[0][0] == player and board[1][1] == player and board[2][2] == player],  # main diag
            [board[0][2] == player and board[1][1] == player and board[2][0] == player]  # second diag
        ]
        return any(any(row) for row in win_conditions)
