# TITLE: Haunted Wasteland
from utils import get_file_contents, plog


INPUT_FILE = 'input/day08.txt'


class Node:
    def __init__(self, node_data):
        node_data = node_data.replace('(', '')
        node_data = node_data.replace(')', '')
        left, right = node_data.split(',')
        self.left = left.strip()
        self. right = right.strip()

    def __str__(self) -> str:
        return f'({self.left}, {self.right})'

    def __repr__(self) -> str:
        return f'({self.left}, {self.right})'


def puzzle_one(raw_data: list) -> int:
    """How many steps are required to reach ZZZ?"""
    directions = raw_data[0]
    raw_data = raw_data[2:]
    network = {}
    for row in raw_data:
        key, node_data = row.split('=')
        key = key.strip()
        network[key] = Node(node_data)
    count = 0
    key = 'AAA'
    while key != 'ZZZ':
        for d in directions:
            if d == 'L':
                key = network[key].left
            else:
                key = network[key].right
            count += 1
            if key == 'ZZZ':
                break
    return count


def puzzle_two(raw_data: list) -> int:
    """TODO"""
    pass


if __name__ == "__main__":
    raw_data = get_file_contents(INPUT_FILE)

    result = puzzle_one(raw_data)
    plog(result)

    result = puzzle_two(raw_data)
    plog(result)
