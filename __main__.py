import validator
from constants import *
import messages
import moves
from board import print_board, create_board
from players import next_player

def play_connect_four():
    board = create_board()
    player = PLAYER_1

    while True:
        print_board(board)
        
        user_input = input(f"Player {player}, choose a column (1-7): ")
        if not validator.is_valid_input(user_input):
            print(messages.INVALID_INPUT)
            continue
        col = int(user_input) - 1

        if validator.is_valid_location(board, col):
            moves.drop_piece(board, col, player)
            if moves.is_winning_move(board, player):
                print_board(board)
                print(messages.WIN.format(player=player))
                break
            if moves.is_draw_move(board):
                print_board(board)
                print(messages.DRAW)
                break
            player = next_player(player)
        else:
            print(messages.INVALID_MOVE)

if __name__ == "__main__":
    play_connect_four()
