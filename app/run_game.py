from app.auto_play import ComputerPlayer
from app.tic_tac_toe import TicTacToe


if __name__ == '__main__':
    user_player = ComputerPlayer('X')
    computer_player = ComputerPlayer('O')
    game = TicTacToe(user_player, computer_player)
    game.start()
