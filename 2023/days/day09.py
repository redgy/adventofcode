# TITLE: Mirage Maintenance
from utils import get_file_contents, plog


INPUT_FILE = 'input/day09.txt'


def get_extrapolated_values(arr_map: list) -> list:
    """After extrapolated values are filled, strictly get those values"""
    extrapolated_values = []
    for arr in arr_map:
        extrapolated_values.append(arr[-1])
    return extrapolated_values


def fill_extrapolated_values(arr_map: list) -> list:
    """Fills extrapolated values in list of lists"""
    last_row = len(arr_map)-1
    last_list = arr_map[last_row]
    last_list.append(0)

    for index, value in enumerate(arr_map, start=1):
        current_index = last_row - index
        if current_index == -1:
            continue
        current_list = arr_map[current_index]
        previous_list = arr_map[current_index+1]
        extrapolated_value = current_list[-1] + previous_list[-1]
        current_list.append(extrapolated_value)
    return arr_map


def get_step_array(arr: list) -> list:
    step_array = []
    for x in range(len(arr)):
        if x == len(arr)-1:
            continue
        step = calculate_step(arr[x], arr[x+1])
        step_array.append(step)
    return step_array


def calculate_step(num1: int, num2: int) -> int:
    return num2 - num1


def puzzle_one(raw_data: list) -> int:
    """What is the sum of extrapolated values?"""
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
