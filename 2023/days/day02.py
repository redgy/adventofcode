# TITLE: Cube Conundrum
from utils import get_file_contents, plog
import re
INPUT_FILE = 'samples/day01.txt'


def is_game_possible(game_record: str) -> bool:
    return -1


def puzzle_one(raw_data: list) -> int:
    """What is the sum of the IDs of possible games?"""
    values = [is_game_possible(x) for x in raw_data]
    return sum(values)


def puzzle_two():
    pass


if __name__ == "__main__":
    raw_data = get_file_contents(INPUT_FILE)

    result = puzzle_one(raw_data)
    plog(result)
