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

    def print_board(self):
        """Prints the current state of the game board to the console."""
        for row in self.board:
            print(row)
