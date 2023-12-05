# TITLE: Cube Conundrum
from utils import get_file_contents, plog
INPUT_FILE = 'input/day02.txt'
RED = 12
BLUE = 14
GREEN = 13


def strip_list(some_list):
    return [x.strip() for x in some_list]


def get_max_game_data(game_record: str) -> dict:
    """From game record, create max game data"""
    game_id_string, all_pulls_string = game_record.split(':')
    game_id = int(game_id_string.split(' ')[1])  # ['Game', 'N']
    max_data = {'red': 0, 'blue': 0, 'green': 0}
    pull_list = strip_list(all_pulls_string.split(';'))
    for cubes_pulled in pull_list:
        single_cubes = strip_list(cubes_pulled.split(','))
        for cube in single_cubes:
            count, color = strip_list(cube.split(' '))
            count = int(count)  # convert string to integer
            if max_data[color] < count:
                max_data[color] = count
    return {game_id: max_data}


def _is_color_possible(color: str, game_data: dict, starting_cubes: dict) -> bool:
    """Compare color counts and make sure does not exceed starting number"""
    return game_data[color] <= starting_cubes[color]


def is_game_possible(game_data: dict, starting_cubes: dict) -> bool:
    """Determine if game is possible"""
    colors = ['red', 'blue', 'green']
    for color in colors:
        if not _is_color_possible(color, game_data, starting_cubes):
            return False
    return True


def puzzle_one(raw_data: list) -> int:
    """What is the sum of the IDs of possible games?"""
    game_records = [get_max_game_data(x) for x in raw_data]
    possible_games = []
    max_data = {'red': RED, 'blue': BLUE, 'green': GREEN}
    for record in game_records:
        for game_id, game_data in record.items():
            if is_game_possible(game_data, max_data):
                possible_games.append(game_id)
    return sum(possible_games)


def calculate_power(game_data: dict) -> int:
    """Multiply max number of each cube color"""
    return -1


def puzzle_two(raw_data: list) -> int:
    """What is the sum of the IDs of possible games?"""
    game_records = [get_max_game_data(x) for x in raw_data]
    possible_games = []
    max_data = {'red': RED, 'blue': BLUE, 'green': GREEN}
    for record in game_records:
        for game_id, game_data in record.items():
            if is_game_possible(game_data, max_data):
                possible_games.append(game_id)
    return sum(possible_games)


def puzzle_two():
    pass


if __name__ == "__main__":
    raw_data = get_file_contents(INPUT_FILE)

    result = puzzle_one(raw_data)
    plog(result)
