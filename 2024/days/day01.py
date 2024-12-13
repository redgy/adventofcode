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


def part_one(raw_data):
    list_one = []
    list_two = []
    for row in raw_data:
        point_a, point_b = [int(x) for x in row.strip().split(' ') if x]
        list_one.append(point_a)
        list_two.append(point_b)

    distances = []
    while list_one:
        min_a, min_b = get_min_pair(list_one, list_two)
        distance = calculate_distance(min_a, min_b)
        distances.append(distance)
        list_one.remove(min_a)
        list_two.remove(min_b)
    return sum(distances)


def main():
    sample_raw_data = read_txt(SAMPLE)
    sample_result = part_one(sample_raw_data)
    print(f'Sample part one: {sample_result}')

    input_raw_data = read_txt(INPUT)
    input_result = part_one(input_raw_data)
    print(f'Input part one: {input_result}')


if __name__ == '__main__':
    main()
