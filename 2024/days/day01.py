# DAY 01 -- HISTORIAN HYSTERIA
from copy import deepcopy
from read_file import read_txt
SAMPLE = 'samples/day01.txt'
INPUT = 'input/day01.txt'


def calculate_distance(point_a: int, point_b: int) -> int:
    if point_a > point_b:
        return point_a - point_b
    return point_b - point_a


def get_min_pair(list_one: list[int], list_two: list[int]) -> tuple[int, int]:
    if len(list_one) != len(list_two):
        raise ValueError('list lengths are different')
    min_one = min(list_one)
    min_two = min(list_two)
    return min_one, min_two


def count_frequency(num: int, list_to_compare: list[int]) -> int:
    """Number of times the number shows up in the list"""
    count = 0
    for x in list_to_compare:
        if x == num:
            count += 1
    return count


def part_one(list_one, list_two):
    list_one = deepcopy(list_one)
    list_two = deepcopy(list_two)
    distances = []
    while list_one:
        min_a, min_b = get_min_pair(list_one, list_two)
        distance = calculate_distance(min_a, min_b)
        distances.append(distance)
        list_one.remove(min_a)
        list_two.remove(min_b)
    return sum(distances)


def part_two(list_one, list_two):
    similarity = []
    for num in list_one:
        count = count_frequency(num, list_two)
        similarity.append(num * count)
    return sum(similarity)


def get_lists(raw_data) -> tuple[list[int], list[int]]:
    list_one = []
    list_two = []
    for row in raw_data:
        point_a, point_b = [int(x) for x in row.strip().split(' ') if x]
        list_one.append(point_a)
        list_two.append(point_b)
    return list_one, list_two


def main():
    sample_raw_data = read_txt(SAMPLE)
    sample_list_one, sample_list_two = get_lists(sample_raw_data)
    input_raw_data = read_txt(INPUT)
    input_list_one, input_list_two = get_lists(input_raw_data)

    sample_result = part_one(sample_list_one, sample_list_two)
    print(f'Sample part one: {sample_result}')
    input_result = part_one(input_list_one, input_list_two)
    print(f'Input part one: {input_result}')

    sample_result = part_two(sample_list_one, sample_list_two)
    print(f'Sample part two: {sample_result}')
    input_result = part_two(input_list_one, input_list_two)
    print(f'Input part two: {input_result}')


if __name__ == '__main__':
    main()
