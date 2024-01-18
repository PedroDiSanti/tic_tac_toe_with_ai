import random


class ComputerPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    @staticmethod
    def is_valid_move(i: int, j: int, board) -> bool:
        if i < 0 or i >= 3 or j < 0 or j >= 3:  # check if the move is within the board
            return False
        if board[i][j] != ' ':  # check if the position is not occupied
            return False
        return True

    def get_move(self, board, symbol):
        valid_moves = []
        for i in range(3):
            for j in range(3):
                if self.is_valid_move(i, j, board):
                    valid_moves.append((i, j))

        # Choose a random move
        move = random.choice(valid_moves)
        print(f"Computer ({symbol}) move: {move}")
        return move
