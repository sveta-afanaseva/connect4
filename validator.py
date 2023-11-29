from constants import COLUMNS, EMPTY_SLOT

def is_valid_input(user_input: str) -> bool:
    try:
        num = int(user_input)
        return 1 <= num <= COLUMNS
    except ValueError:
        return False
    
def is_valid_location(board: list[list[str]], col: int) -> bool:
    return board[0][col] == EMPTY_SLOT
