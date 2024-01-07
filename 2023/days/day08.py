# TITLE: Haunted Wasteland
from utils import get_file_contents, plog


INPUT_FILE = 'samples/day08-1.txt'


class Node:
    def __init__(self, left: str, right: str):
        self.left = left
        self. right = right


class Network:
    def __init__(self):
        pass


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
