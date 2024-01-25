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

    def __init__(self, player1, player2, board):
        """The constructor method which initializes the board and players."""
        self.render_board = board
        self.players = [player1, player2]

    def start(self):
        """
        Method to start the game.

        :return: None
        """
        player_index = 0
        self.render_board.print_board(self.render_board.board)

        while True:
            current_player = self.players[player_index]

            move_i, move_j = current_player.get_move(self.render_board.board, current_player.symbol)

            self.render_board.board[move_i][move_j] = current_player.symbol
            self.render_board.print_board(self.render_board.board)

            player_index = (player_index + 1) % 2

            if self.render_board.check_win(self.render_board.board, current_player.symbol):
                print(f"{current_player.symbol} Wins!")
                return
