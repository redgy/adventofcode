# TITLE: Mirage Maintenance
from utils import get_file_contents, plog


INPUT_FILE = 'input/day09.txt'


def get_extrapolated_values(arr_map: list) -> list:
    """After extrapolated values are filled, strictly get those values"""
    pass


def fill_extrapolated_values(arr_map: list) -> list:
    """Fills extrapolated values in list of lists"""
    pass


def get_step_array(arr: list) -> list:
    pass


def calculate_step(num1: int, num2: int) -> int:
    pass


def puzzle_one(raw_data: list) -> int:
    """What is the sum of extrapolated values?"""
    pass


def puzzle_two(raw_data: list) -> int:
    """TODO"""
    pass


if __name__ == "__main__":
    raw_data = get_file_contents(INPUT_FILE)

    result = puzzle_one(raw_data)
    plog(result)

    result = puzzle_two(raw_data)
    plog(result)
