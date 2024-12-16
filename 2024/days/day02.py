# DAY 02 -- RED-NOSED REPORTS
from read_file import read_txt


SAMPLE = 'samples/day02.txt'
INPUT = 'input/day02.txt'


def get_is_increasing_list(array: list[int]) -> list[bool]:
    array_pairs = zip(array, array[1:])  # pair first item with next item in list
    return [num_one < num_two for num_one, num_two in array_pairs]


def is_all_increasing(array: list[int]) -> bool:
    increasing_list = get_is_increasing_list(array)
    return all(increasing_list)


def get_is_decreasing_list(array: list[int]) -> list[bool]:
    array_pairs = zip(array, array[1:])  # pair first item with next item in list
    return [num_one > num_two for num_one, num_two in array_pairs]


def is_all_decreasing(array: list[int]) -> bool:
    decreasing_list = get_is_decreasing_list(array)
    return all(decreasing_list)


def get_difference(x: int, y: int) -> int:
    if x > y:
        return x - y
    return y - x


def is_safe(array: list[int]) -> bool:
    if not is_all_increasing(array) and not is_all_decreasing(array):
        return False
    array_pairs = zip(array, array[1:])  # pair first item with next item in list
    return all(
        get_difference(num_one, num_two) >= 1 and
        get_difference(num_one, num_two) <= 3
        for num_one, num_two in array_pairs)


def get_reports(raw_data) -> list[list]:
    reports = []
    for row in raw_data:
        clean_row = row.strip().split(' ')
        reports.append([int(x) for x in clean_row if x])
    return reports


def get_list_ranking(array: list[int]) -> int:
    """Is the list increasing, decreasing, or neither?

    If decreasing: return -1
    If increasing: return 1
    If neither: return 0
    """
    is_increasing_list = get_is_increasing_list(array)
    is_decreasing_list = get_is_decreasing_list(array)
    num_increasing = sum([1 for x in is_increasing_list if x])
    num_decreasing = sum([1 for x in is_decreasing_list if x])
    if num_decreasing > num_increasing:
        return -1
    if num_increasing > num_decreasing:
        return 1
    return 0


def _remove_first_or_second_from_list(array: list[int], index: int) -> list[int]:
    """Helper method to remove first or second from list"""
    remove_num_one = array[:index] + array[index+1:]
    remove_num_two = array[:index+1] + array[index+2:]
    if is_safe(remove_num_one):
        return remove_num_one
    return remove_num_two


def remove_one_unsafe_level(array: list[int]) -> list[int]:
    array_pairs = zip(array, array[1:])  # pair first item with next item in list
    ranking_type = get_list_ranking(array)
    if ranking_type == 0:  # neither increasing or decreasing
        return array
    for index, (num_one, num_two) in enumerate(array_pairs):
        if num_one == num_two:
            del array[index+1]
            return array
        match ranking_type:
            case -1:  # decreasing
                if num_one < num_two:
                    return _remove_first_or_second_from_list(array, index)
            case 1:  # increasing
                if num_one > num_two:
                    return _remove_first_or_second_from_list(array, index)
    array_pairs = zip(array, array[1:])  # pair first item with next item in list
    for index, (num_one, num_two) in enumerate(array_pairs):
        num_diff = get_difference(num_one, num_two)
        is_out_of_bounds = num_diff > 3 or num_diff < 1
        if is_out_of_bounds:
            return _remove_first_or_second_from_list(array, index)
    return array


def part_one(reports):
    is_safe_list = [1 for report in reports if is_safe(report)]
    return sum(is_safe_list)


def part_two(reports):
    is_safe_list = []
    for report in reports:
        if is_safe(report):
            is_safe_list.append(report)
            continue
        report_minus_one = remove_one_unsafe_level(report)
        if is_safe(report_minus_one):
            is_safe_list.append(report_minus_one)
            continue
    return len(is_safe_list)


def main():
    sample_raw_data = read_txt(SAMPLE)
    sample_data = get_reports(sample_raw_data)
    input_raw_data = read_txt(INPUT)
    input_data = get_reports(input_raw_data)

    sample_result = part_one(sample_data)
    print(f'Sample result part one: {sample_result}')
    input_result = part_one(input_data)
    print(f'Input result part one: {input_result}')

    sample_result = part_two(sample_data)
    print(f'Sample result part two: {sample_result}')
    input_result = part_two(input_data)
    print(f'Input result part two: {input_result}')


if __name__ == '__main__':
    main()
