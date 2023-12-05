from utils import get_file_contents, plog
INPUT_FILE = 'input/day01.txt'
# TITLE: Trebuchet?!


def calibrate(line: str) -> int:
    """Take a string return the first and last digit"""
    integers = [c for c in line if c.isdigit()]
    num_string = ""
    if not integers:
        num_string = 0
    elif len(integers) == 1:
        num_string = f'{integers[0]}{integers[0]}'
    else:
        num_string = f'{integers[0]}{integers[-1]}'
    return int(num_string)


def puzzle_one(raw_data: list) -> int:
    """What is the sum of all of the calibration values?"""
    values = [calibrate(x) for x in raw_data]
    return sum(values)


if __name__ == "__main__":
    raw_data = get_file_contents(INPUT_FILE)
    result = puzzle_one(raw_data)
    plog(result)
