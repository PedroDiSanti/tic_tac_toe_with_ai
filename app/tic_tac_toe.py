class TicTacToe:
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

    def __init__(self, player1, player2):
        """The constructor method which initializes the board and players."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.players = [player1, player2]

    def print_board(self):
        """Prints the current state of the game board to the console."""
        for row in self.board:
            print(row)

    def check_win(self, player: str):
        """
        Checks if the specified player has won the game.

        Args:
        player (str): The symbol of the player to check for a win.

        Returns:
        bool: True if the player has won, False otherwise.
        """
        # check horizontal, vertical, and diagonal winning conditions
        win_conditions = [
            [self.board[0][j] == player and self.board[1][j] == player and self.board[2][j] == player for j in
             range(3)],  # columns
            [self.board[i][0] == player and self.board[i][1] == player and self.board[i][2] == player for i in
             range(3)],  # rows
            [self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player],  # main diag
            [self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player]  # second diag
        ]
        return any(any(row) for row in win_conditions)

    def start(self):
        """Starts the game, alternating between players until a winning condition is met."""
        player_index = 0
        self.print_board()

        while True:
            while True:
                current_player = self.players[player_index]
                print(f"It's {current_player.symbol}'s turn.")

                move_i, move_j = current_player.get_move(self.board, current_player.symbol)

                self.board[move_i][move_j] = current_player.symbol
                self.print_board()

                if self.check_win(current_player.symbol):
                    print(f"{current_player.symbol} Wins!")
                    return

                player_index = (player_index + 1) % 2