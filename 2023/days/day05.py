# TITLE: If You Give A Seed A Fertilizer
from utils import get_file_contents, clean_list, convert_str_to_int, plog
import re
INPUT_FILE = 'samples/day05.txt'


def parse_data(raw_data: list) -> dict:
    seed_list = raw_data[0]
    parsed_map = {'seeds': seed_list}
    raw_map_data = clean_list(raw_data[2:])
    raw_map_data.reverse()  # go backwards
    numbers_list = []
    for row in raw_map_data:
        is_not_map_title = row.find('map:') == -1
        if is_not_map_title:
            convert_numbers = row.split(' ')
            numbers_list.extend(convert_numbers)
        else:
            map_title = row.split(' ')[0]
            parsed_map[map_title] = numbers_list
            numbers_list = []
    return parsed_map


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
