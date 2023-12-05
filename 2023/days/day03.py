# TITLE: Gear Ratios
from utils import get_file_contents, plog
INPUT_FILE = 'input/day02.txt'


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


def is_adjacent_to_symbol(row: int, col: int, matrix: list) -> bool:
    """Note: periods (.) are not symbols"""
    return False


def is_part_number(row: int, start: int, end: int) -> bool:
    """If adjacent to symbol, then it is a part number

    :param row: Row number is on
    :param start: Starting index of number
    :param end: Ending index of number
    """
    return False


def puzzle_one(raw_data: list) -> int:
    """What is the sum of all part numbers in schematic?"""
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
