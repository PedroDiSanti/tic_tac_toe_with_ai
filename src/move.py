from src.logic import Logic


class Move:
    """
    Checks if the identified move (i, j) is valid on the provided game board.

    :param i: The row of the move.
    :param j: The column of the move.
    :param board: The current state of the game board.
    :return: True if the move is valid, False otherwise.
    """

    def __init__(self):
        """

        __init__()

        Initialize the object by creating an instance of the Logic class and setting the depth to 0.

        Parameters:
        - self: The object itself.

        Returns:
        This method does not return anything.

        """
        self.logic = Logic()
        self.depth = 0

    @staticmethod
    def is_valid_move(i: int, j: int, board: list) -> bool:
        """
        Check if a move is valid on the board.

        :param i: The row index of the move.
        :param j: The column index of the move.
        :param board: The current state of the board.
        :return: True if the move is valid, False otherwise.
        """
        if i < 0 or i >= 3 or j < 0 or j >= 3:
            return False
        if board[i][j] != ' ':
            return False
        return True

    def get_move(self, board: list, symbol: str) -> list:
        """
        :param board: The game board
        :param symbol: The symbol of the player making the move
        :return: The move chosen by the player or generated automatically

        This method allows a player to choose their move or generates an automatic move if the player is not "O".
        If the player is "O", the move is generated automatically using the _generate_auto_move() method.
        Otherwise, the player is prompted to enter their move using the _generate_player_move() method.

        The chosen move is then printed along with the symbol of the player.
        Finally, the chosen move is returned.
        """
        if symbol == "O":
            move = self._generate_auto_move(board)
        else:
            move = self._generate_player_move(board)

        print(f"({symbol}) move: {move}")
        return move

    def _generate_player_move(self, board: list) -> list:
        """
        :param board: The current state of the game board.
        :return: A list representing the player's move, in the format [row, col].

        This method prompts the player for their move and validates whether the move is valid or not. The player should enter their move in the format (row, col), separated by a comma. The user
        * input is then split into two integers, representing the row and column of the move. If the move is valid, it is returned as a list [row, col].
        """
        while True:
            print("It's X turn. Enter your move in the format (row, col):")
            move = input()
            i, j = map(int, move.split(','))
            if self.is_valid_move(i, j, board):
                return [i, j]

    def _generate_auto_move(self, board: list) -> list:
        """
        :param board: The current state of the game board.
        :param valid_moves: A list of valid moves.
        :return: The chosen move as a tuple (row, column).

        This method is responsible for generating an automatic move for the game. It iterates through each cell of the game board and checks if it is a valid move using the `is_valid_move` method
        *. If a cell is a valid move, it adds it to the `valid_moves` list. Finally, it selects a random move from the `valid_moves` list and returns it as the chosen move.

        Example usage:
            board = [['X', 'O', ''],
                     ['', 'X', 'O'],
                     ['', '', '']]
            valid_moves = []
            game._generate_auto_move(board, valid_moves)
            # Returns a random valid move (e.g., (0, 2))
        """
        move = self.logic.determine_best_score_and_move(board, self.depth, True, 'O')
        i, j = move.get("index")[0], move.get("index")[1]
        return [i, j]
