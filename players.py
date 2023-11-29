from constants import PLAYER_1, PLAYER_2

def next_player(player):
    return PLAYER_2 if player == PLAYER_1 else PLAYER_1
