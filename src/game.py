from src.board import Board
from src.move import Move


class Game:
    """
    The main class implementing the game of Tic Tac Toe.

    Attributes:
    board (list of str): The game board, a 3x3 matrix.
    players (list of Player): The players participating in the game.

    Methods:
    print_board(): Prints the current state of the board.
    check_win(player: str): Checks if the specified player has won the game.
    start(): Starts the game loop, alternating between players until a winning condition is met.
    """

    def __init__(self):
        """The constructor method which initializes the board and players."""
        self.board = Board()
        self.move = Move()
        self.players = ['X', 'O']

    def start(self):
        """
        Method to start the game.

        :return: None
        """
        player_index = 0
        self.board.print_board(self.board.board)

        while True:
            symbol = self.players[player_index]

            move_i, move_j = self.move.get_move(self.board.board, symbol)

            self.board.board[move_i][move_j] = symbol
            self.board.print_board(self.board.board)

            player_index = (player_index + 1) % 2

            if self.board.check_win(self.board.board, symbol):
                print(f"{symbol} Wins!")
                return
