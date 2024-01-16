# Tic Tac Toe Game

This project is a simple implementation of the popular game "Tic Tac Toe" developed in Python.

## Technology Used

- Python 3.10.4: Our version of choice due to its clear syntax, vast library support, and powerful features.
- Pytest: A testing framework for Python that allows the easy creation of simple and scalable tests.

## How it Works

The game is run through the `TicTacToe` class, which manages what player's move is next, validation of the player's move, and determining if a game-winning condition has been met on each move.

### Overview of Key Methods:

- `start()`: This method begins the game, taking input from the players for their moves, validating the moves, updating the board, and checking for a winner.
- `is_valid_move(i, j)`: This method checks if a player's move is valid (i.e., within the board and on an empty space).
- `print_board()`: This method prints the current game board to the console.
- `check_win(player)`: This method checks if the passed player has any three-in-row on the board (`True` indicates a win, `False` indicates no win yet).
- `change_player()`: This method switches the active player.

## How to Run the Project

1. Clone the repository to your local machine.
2. Ensure you have Python 3.10.4 installed (you can download it from [here](https://www.python.org/downloads/)).
3. Navigate to the directory where you cloned the repository via the command prompt.
4. Run the command - `python tictactoe.py`.

## Testing

To run tests, ensure you have pytest installed (`pip install pytest`), navigate to the directory with the tests in your terminal, and run `pytest`.

---

Happy coding, and we hope you enjoy the game!