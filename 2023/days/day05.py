# TITLE: If You Give A Seed A Fertilizer
from utils import get_file_contents, clean_list, convert_str_to_int, plog
import re
INPUT_FILE = 'input/day05.txt'


def parse_data(raw_data: list) -> dict:
    first_row = raw_data[0]  # "seeds: N, N, N, N"
    seed_list = first_row.split(' ')[1:]
    parsed_map = {'seeds': seed_list}
    raw_map_data = clean_list(raw_data[2:])
    raw_map_data.reverse()  # go backwards
    numbers_list = []
    for row in raw_map_data:
        is_not_map_title = row.find('map:') == -1
        if is_not_map_title:
            convert_numbers = row.split(' ')
            int_numbers = [int(x) for x in convert_numbers]
            numbers_list.append(int_numbers)
        else:
            map_title = row.split(' ')[0]
            parsed_map[map_title] = numbers_list
            numbers_list = []
    return parsed_map


def create_map(destination_start: int, source_start: int, range_length: int) -> dict:
    """Source -> Destination map"""
    return {source_start+x: destination_start+x for x in range(range_length)}


def create_almanac(parsed_data: dict):
    almanac = {k: {} for k in parsed_data.keys()}
    for key, nested_list in parsed_data.items():
        if key == 'seeds':
            continue
        key_map = {}
        for triplet in nested_list:
            new_map = create_map(triplet[0], triplet[1], triplet[2])
            key_map.update(new_map)
        almanac[key] = key_map
    return almanac


def get_from_almanac(almanac_key: str, dict_key: int, almanac: dict):
    """Get value from almanac given a key (e.g. seed-to-soil) and dict key (e.g. 12)"""
    return almanac[almanac_key].get(dict_key, dict_key)


def get_soil(starting_seed: int, almanac: dict):
    """From starting seed, go through all of almanac and return fertilizer number"""
    return get_from_almanac('seed-to-soil', starting_seed, almanac)


def get_fertilizer(starting_seed: int, almanac: dict):
    """From starting seed, go through all of almanac and return fertilizer number"""
    soil = get_soil(starting_seed, almanac)
    fertilizer = get_from_almanac('soil-to-fertilizer', soil, almanac)
    return fertilizer


def get_water(starting_seed: int, almanac: dict):
    """From starting seed, go through all of almanac and return water number"""
    fertilizer = get_fertilizer(starting_seed, almanac)
    water = get_from_almanac('fertilizer-to-water', fertilizer, almanac)
    return water


def get_light(starting_seed: int, almanac: dict):
    """From starting seed, go through all of almanac and return light number"""
    water = get_water(starting_seed, almanac)
    light = get_from_almanac('water-to-light', water, almanac)
    return light


def get_temperature(starting_seed: int, almanac: dict):
    """From starting seed, go through all of almanac and return temperature number"""
    light = get_light(starting_seed, almanac)
    temperature = get_from_almanac('light-to-temperature', light, almanac)
    return temperature


def get_humidity(starting_seed: int, almanac: dict):
    """From starting seed, go through all of almanac and return humidity number"""
    temperature = get_temperature(starting_seed, almanac)
    humidity = get_from_almanac('temperature-to-humidity', temperature, almanac)
    return humidity


def get_location(starting_seed: int, almanac: dict):
    """From starting seed, go through all of almanac and return location number"""
    humidity = get_humidity(starting_seed, almanac)
    location = get_from_almanac('humidity-to-location', humidity, almanac)
    return location


def puzzle_one(raw_data: list) -> int:
    """What is the lowest location number that corresponds to any of the initial seed numbers?"""
    parsed_data = parse_data(raw_data)
    seeds = parsed_data['seeds']
    almanac = create_almanac(parsed_data)
    locations = []
    for seed in seeds:
        location = get_location(seed, almanac)
        locations.append(int(location))
    return min(locations)


def puzzle_two(raw_data: list) -> int:
    """TODO"""
    pass


if __name__ == "__main__":
    raw_data = get_file_contents(INPUT_FILE)

    result = puzzle_one(raw_data)
    plog(result)

    result = puzzle_two(raw_data)
    plog(result)
