# TITLE: Scratchcards
from utils import get_file_contents, plog
import re
INPUT_FILE = 'input/day03.txt'


def get_matching_winning_numbers(your_numbers: list, winning_numbers: list) -> list:
    """Compare two lists and get winning matches

    :param your_numbers: List of your numbers
    :param winning_numbers: List of winning numbers
    :returns: List of matching winning numbers
    """
    return list(set(your_numbers).intersection(set(winning_numbers)))


def calculate_points(winning_numbers: list) -> int:
    """From a list of matching winning numbers, calculate the points"""
    # challenge to self: can you do this without multiplying?
    if not winning_numbers:
        return 0
    if len(winning_numbers) == 1:
        return 1
    points = 1
    for num in winning_numbers[1:]:
        points += points
    return points


def puzzle_one(raw_data: list) -> int:
    pass


def puzzle_two(raw_data: list) -> int:
    pass


if __name__ == "__main__":
    raw_data = get_file_contents(INPUT_FILE)

    # result = puzzle_one(raw_data)
    # plog(result)

    # result = puzzle_two(raw_data)
    # plog(result)
