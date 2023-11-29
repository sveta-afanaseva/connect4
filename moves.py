from constants import ROWS, COLUMNS, EMPTY_SLOT

def drop_piece(board: list[list[str]], col:int, player: str) -> None:
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY_SLOT:
            board[row][col] = player
            break
        
def is_draw_move(board: list[list[str]]) -> bool:
    return all([elem != EMPTY_SLOT for row in board for elem in row])

def is_winning_move(board: list[list[str]], player: str) -> bool:
    # Check horizontally
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if (
                board[row][col] == player and
                board[row][col + 1] == player and
                board[row][col + 2] == player and
                board[row][col + 3] == player
            ):
                return True

    # Check vertically
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if (
                board[row][col] == player and
                board[row + 1][col] == player and
                board[row + 2][col] == player and
                board[row + 3][col] == player
            ):
                return True

    # Check diagonally (positive slope)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if (
                board[row][col] == player and
                board[row + 1][col + 1] == player and
                board[row + 2][col + 2] == player and
                board[row + 3][col + 3] == player
            ):
                return True

    # Check diagonally (negative slope)
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if (
                board[row][col] == player and
                board[row - 1][col + 1] == player and
                board[row - 2][col + 2] == player and
                board[row - 3][col + 3] == player
            ):
                return True

    return False
