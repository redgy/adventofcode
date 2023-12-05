# TITLE: Cube Conundrum
from utils import get_file_contents, plog
INPUT_FILE = 'samples/day02.txt'


def get_max_game_data(game_record: str) -> dict:
    """From game record, create max game data"""
    return {}


def is_game_possible(max_game_data: dict, starting_cubes: dict) -> bool:
    """Determine if game is possible"""
    return False


def puzzle_one(raw_data: list) -> int:
    """What is the sum of the IDs of possible games?"""
    game_records = [get_max_game_data(x) for x in raw_data]
    possible_games = []
    for record in game_records:
        for game_id, max_data in record.items():
            if is_game_possible(max_data):
                possible_games.append(game_id)
    return sum(possible_games)


def puzzle_two():
    pass


if __name__ == "__main__":
    raw_data = get_file_contents(INPUT_FILE)

    result = puzzle_one(raw_data)
    plog(result)
