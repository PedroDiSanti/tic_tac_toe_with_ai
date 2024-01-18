class TicTacToe:
    def __init__(self, player1, player2):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.players = [player1, player2]

    def print_board(self):
        for row in self.board:
            print(row)

    def check_win(self, player):
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

