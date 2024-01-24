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

    def check_win(self, player: str):
        """
        Checks if the specified player has won the game.

        Args:
        player (str): The symbol of the player to check for a win.

        Returns:
        bool: True if the player has won, False otherwise.
        """
        win_conditions = [
            [self.render_board.board[0][j] == player and self.render_board.board[1][j] == player and
             self.render_board.board[2][j] == player for j in range(3)],  # columns
            [self.render_board.board[i][0] == player and self.render_board.board[i][1] == player and
             self.render_board.board[i][2] == player for i in range(3)],  # rows
            [self.render_board.board[0][0] == player and self.render_board.board[1][1] == player and
             self.render_board.board[2][2] == player],  # main diag
            [self.render_board.board[0][2] == player and self.render_board.board[1][1] == player and
             self.render_board.board[2][0] == player]  # second diag
        ]
        return any(any(row) for row in win_conditions)

    def start(self):
        """
        Method to start the game.

        :return: None
        """
        player_index = 0
        self.render_board.print_board()

        while True:
            current_player = self.players[player_index]
            print(f"It's {current_player.symbol}'s turn.")

            move_i, move_j = current_player.get_move(self.render_board.board, current_player.symbol)

            self.render_board.board[move_i][move_j] = current_player.symbol
            self.render_board.print_board()

            player_index = (player_index + 1) % 2

            if self.check_win(current_player.symbol):
                print(f"{current_player.symbol} Wins!")
                return
