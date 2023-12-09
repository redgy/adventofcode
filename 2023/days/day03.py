# TITLE: Gear Ratios
from utils import get_file_contents, plog
import re
INPUT_FILE = 'input/day03.txt'


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
    is_longer_than_length = row >= len(matrix) or col >= len(matrix[row])
    return (is_negative or is_longer_than_length)


def _check_adjacent(row: int, col: int, matrix: list, check_symbol=True) -> bool:
    """Helper method to check the passed in adjacent 'cell'

    :param row: Row the cell is on
    :param col: Columng the cell is on
    :param matrix: List of lists, the matrix
    :param check_symbol: True == checks if symbol; False == checks if digit
    """
    if not is_out_of_bounds(row, col, matrix):
        character = matrix[row][col]
        if check_symbol:
            return is_symbol(character)
        else:
            try:
                int(character)
            except ValueError:
                return False
            return True
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
    if _check_adjacent(row, col+1, matrix):  # right
        is_adjacent = True
    if _check_adjacent(row+1, col-1, matrix):  # diagonal down left
        is_adjacent = True
    if _check_adjacent(row+1, col, matrix):  # down
        is_adjacent = True
    if _check_adjacent(row+1, col+1, matrix):  # diagonal down right
        is_adjacent = True
    return is_adjacent


def get_number(row: list, index: int) -> int:
    """From row in matrix, get the number found around the index

    :param row: List of characters in a row in the matrix
    :param index: Index where adjacent digit was found
    :returns: The number
    """
    row_string = "".join(row)
    character = row_string[index]
    number_string = f'{character}' if character.isdigit() else ''
    # go left
    moving_index = index-1
    while moving_index >= 0:
        character = row_string[moving_index]
        if character.isdigit():
            number_string = f'{character}{number_string}'
            moving_index -= 1
        else:
            moving_index = -1
    # go right
    moving_index = index+1
    while moving_index < len(row_string):
        character = row_string[moving_index]
        if character.isdigit():
            number_string = f'{number_string}{character}'
            moving_index += 1
        else:
            moving_index = len(row_string)
    return int(number_string)


def get_adjacent_part_numbers(row: int, col: int, matrix: list) -> list:
    """Get adjacent part numbers

    :param row: Row the potential gear is on
    :param col: Column the potential gear is on
    :param matrix: The matrix
    :returns: List of part numbers the potential gear has
    """
    part_numbers = []
    if _check_adjacent(row-1, col-1, matrix, check_symbol=False):  # diagonal up left
        part_numbers.append(get_number(matrix[row-1], col-1))
    if _check_adjacent(row-1, col, matrix, check_symbol=False):  # up
        part_numbers.append(get_number(matrix[row-1], col))
    if _check_adjacent(row-1, col+1, matrix, check_symbol=False):  # diagonal up right
        part_numbers.append(get_number(matrix[row-1], col+1))
    if _check_adjacent(row, col-1, matrix, check_symbol=False):  # left
        part_numbers.append(get_number(matrix[row], col-1))
    if _check_adjacent(row, col+1, matrix, check_symbol=False):  # right
        part_numbers.append(get_number(matrix[row], col+1))
    if _check_adjacent(row+1, col-1, matrix, check_symbol=False):  # diagonal down left
        part_numbers.append(get_number(matrix[row+1], col-1))
    if _check_adjacent(row+1, col, matrix, check_symbol=False):  # down
        part_numbers.append(get_number(matrix[row+1], col))
    if _check_adjacent(row+1, col+1, matrix, check_symbol=False):  # diagonal down right
        part_numbers.append(get_number(matrix[row+1], col+1))
    return list(set(part_numbers))  # unique


def is_part_number(matrix: list, row: int, start: int, end: int) -> bool:
    """If adjacent to symbol, then it is a part number

    :param matrix: Matrix to use
    :param row: Row number is on
    :param start: Starting index of number
    :param end: Ending index of number
    """
    for x in range(end-start):
        if is_adjacent_to_symbol(row, start+x, matrix):
            return True
    return False


def puzzle_one(raw_data: list) -> int:
    """What is the sum of all part numbers in schematic?"""
    matrix = create_matrix(raw_data)
    part_numbers = []
    for row, line in enumerate(raw_data):
        matches = re.findall(r'\d+', line)
        end_index = 0
        for match in matches:
            start_index = line.find(match, end_index)
            end_index = start_index + len(match)
            if is_part_number(matrix, row, start_index, end_index):
                part_numbers.append(int(match))
    return sum(part_numbers)


def puzzle_two(raw_data: list) -> int:
    """What is the sum of all the gear ratios in the engine schematic?"""
    matrix = create_matrix(raw_data)
    gears = []
    for row, line in enumerate(raw_data):
        matches = re.finditer(r'\*', line)
        if matches:
            for match in matches:
                col = match.start()
                part_numbers = get_adjacent_part_numbers(row, col, matrix)
                if len(part_numbers) != 2:
                    continue
                product = part_numbers[0] * part_numbers[1]
                gears.append(product)
        else:
            print('SKIPPING')
    return sum(gears)


if __name__ == "__main__":
    raw_data = get_file_contents(INPUT_FILE)

    result = puzzle_one(raw_data)
    plog(result)

    result = puzzle_two(raw_data)
    plog(result)
