# TITLE: Gear Ratios
from utils import get_file_contents, plog
INPUT_FILE = 'samples/day03.txt'


def create_matrix(raw_data: list) -> list:
    """Create a matrix (list of lists)"""
    matrix = []
    for row in raw_data:
        characters = list(row)
        matrix.append(characters)
    return matrix


def is_symbol(char: str) -> bool:
    """Checks if character is a symbol"""
    return not (char.isalnum() or char == '.')


def is_out_of_bounds(row: int, col: int, matrix: list) -> bool:
    """Checks if coordinates are out of bounds"""
    is_negative = row < 0 or col < 0
    is_longer_than_length = col >= len(matrix) or row >= len(matrix[col])
    return (is_negative or is_longer_than_length)


def _check_adjacent(row: int, col: int, matrix: list) -> bool:
    """Helper method to check the passed in adjacent 'cell' is a symbol"""
    if not is_out_of_bounds(row, col, matrix):
        return is_symbol(matrix[col][row])
    return False


def is_adjacent_to_symbol(row: int, col: int, matrix: list) -> bool:
    """Note: periods (.) are not symbols"""
    is_adjacent = False
    if _check_adjacent(row-1, col-1, matrix):  # diagonal up left
        is_adjacent = True
    if _check_adjacent(row-1, col, matrix):  # up
        is_adjacent = True
    if _check_adjacent(row-1, col+1, matrix):  # diagonal up right
        is_adjacent = True
    if _check_adjacent(row, col-1, matrix):  # left
        is_adjacent = True
    if _check_adjacent(row+1, col+1, matrix):  # right
        is_adjacent = True
    if _check_adjacent(row+1, col-1, matrix):  # diagonal down left
        is_adjacent = True
    if _check_adjacent(row+1, col+1, matrix):  # diagonal down right
        is_adjacent = True
    return is_adjacent


def is_part_number(row: int, start: int, end: int) -> bool:
    """If adjacent to symbol, then it is a part number

    :param row: Row number is on
    :param start: Starting index of number
    :param end: Ending index of number
    """
    return False


def puzzle_one(raw_data: list) -> int:
    """What is the sum of all part numbers in schematic?"""
    matrix = create_matrix(raw_data)
    # simply saving code from day 2 in case i can reuse this pattern
    # game_records = [get_max_game_data(x) for x in raw_data]
    # possible_games = []
    # max_data = {'red': RED, 'blue': BLUE, 'green': GREEN}
    # for record in game_records:
    #     for game_id, game_data in record.items():
    #         if is_game_possible(game_data, max_data):
    #             possible_games.append(game_id)
    # return sum(possible_games)
    return -1


def puzzle_two(raw_data: list) -> int:
    """TODO: wait"""
    return -1


if __name__ == "__main__":
    raw_data = get_file_contents(INPUT_FILE)

    result = puzzle_one(raw_data)
    plog(result)

    result = puzzle_two(raw_data)
    plog(result)
