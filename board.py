from constants import EMPTY_SLOT, COLUMNS, ROWS

def create_board() -> list[list[str]]:
    return [[EMPTY_SLOT for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board:list[list[str]]) -> None:
    for row in board:
        print(' '.join(row))
    print(" ".join(map(str, range(1, COLUMNS + 1))))
