# TITLE: Cube Conundrum
from utils import get_file_contents, plog
import re
INPUT_FILE = 'samples/day01.txt'


def get_max_game_data(game_record: str) -> dict:
    """From game record, create max game data"""
    return -1


def is_game_possible(max_game_data: dict, starting_cubes: dict) -> bool:
    """Determine if game is possible"""
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
