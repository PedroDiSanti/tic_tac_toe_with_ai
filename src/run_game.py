from src.app.move import Move
from src.app.board import Board
from src.app.game import Game


if __name__ == '__main__':
    user_player, computer_player = Move('X'), Move('O')
    board = Board()
    game = Game(user_player, computer_player, board)
    game.start()
