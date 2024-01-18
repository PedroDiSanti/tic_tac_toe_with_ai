from app.auto_play import AutoPlay
from app.tic_tac_toe import TicTacToe


if __name__ == '__main__':
    user_player = AutoPlay('X')
    computer_player = AutoPlay('O')
    game = TicTacToe(user_player, computer_player)
    game.start()
