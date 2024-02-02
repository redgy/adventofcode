# TITLE: Mirage Maintenance
from utils import get_file_contents, plog


INPUT_FILE = 'input/day08.txt'


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
