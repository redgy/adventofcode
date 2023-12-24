# TITLE: Wait For It
from utils import get_file_contents, clean_list, convert_str_to_int, plog
import re
INPUT_FILE = 'samples/day06.txt'


def calculate_distance(time_held: int, race_time: int):
    """Calculate distance in race

    :param int time_held: Amount of time button was held
    :param int race_time: Length of race time
    """
    return time_held * (race_time - time_held)


def puzzle_one(raw_data: list) -> int:
    """TODO"""
    return


def puzzle_two(raw_data: list) -> int:
    """TODO"""
    return


if __name__ == "__main__":
    raw_data = get_file_contents(INPUT_FILE)

    result = puzzle_one(raw_data)
    plog(result)

    result = puzzle_two(raw_data)
    plog(result)
