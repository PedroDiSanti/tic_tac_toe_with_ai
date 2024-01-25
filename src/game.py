from src.board import Board
from src.move import Move


class Game:
    """
    Represents a Tic-Tac-Toe game.
    """

    def __init__(self):
        """
        Initializes an instance of the class.

        :param self: The class instance.
        :rtype: None
        """
        self.board = Board()
        self.move = Move()
        self.players = ['X', 'O']

    def start(self):
        """
        Start the game by alternating player turns.

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
            if self.board.is_board_full(self.board.board):
                print("The game is draw!")
                return
