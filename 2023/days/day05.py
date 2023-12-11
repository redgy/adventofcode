# TITLE: If You Give A Seed A Fertilizer
from utils import get_file_contents, clean_list, convert_str_to_int, plog
import re
INPUT_FILE = 'samples/day05.txt'


def parse_data(raw_data: list) -> dict:
    seed_list = raw_data[0]
    plog(clean_list(raw_data[2:]))
    return {}


def create_map(destination_start: int, source_start: int, range_length: int) -> dict:
    """Source -> Destination map"""
    return {source_start+x: destination_start+x for x in range(range_length)}


def puzzle_one(raw_data: list) -> int:
    """TODO"""
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
