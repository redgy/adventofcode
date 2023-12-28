# TITLE: Wait For It
from utils import get_file_contents, clean_list, plog
import re
INPUT_FILE = 'input/day06.txt'


def calculate_distance(time_held: int, race_time: int):
    """Calculate distance in race

    :param int time_held: Amount of time button was held
    :param int race_time: Length of race time
    """
    return time_held * (race_time - time_held)


def puzzle_one(raw_data: list) -> int:
    """What do you get if you multiply these numbers together?"""
    race_times = [int(x) for x in clean_list(raw_data[0].split(' '))[1:]]
    record_distances = [int(x) for x in clean_list(raw_data[1].split(' '))[1:]]
    ways_to_win = []
    for race_num, race_time in enumerate(race_times):
        record_to_beat = record_distances[race_num]
        winning_races = []
        for hold_time in range(race_time):
            distance = calculate_distance(hold_time, race_time)
            if distance > record_to_beat:
                winning_races.append(distance)
        ways_to_win.append(len(winning_races))
    product = 1
    for p in ways_to_win:
        product *= p
    return product


def puzzle_two(raw_data: list) -> int:
    """TODO"""
    return


if __name__ == "__main__":
    raw_data = get_file_contents(INPUT_FILE)

    result = puzzle_one(raw_data)
    plog(result)

    result = puzzle_two(raw_data)
    plog(result)
