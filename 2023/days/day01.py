# TITLE: Trebuchet?!
from utils import get_file_contents, plog
import re
INPUT_FILE = 'input/day01.txt'
VALID_DIGIT_MAPPING = {
    # "zero": 0  # zero is not included in valid digit list
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


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


def replace_words_with_digits(line: str) -> str:
    """Numbers written out from 1-9 should be replaced with its digit counterpart"""
    matches = re.findall(r"(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)", line)
    if not matches:
        return line
    for tuple_match in matches:
        for word in tuple_match:
            if not word:
                continue
            line = line.replace(word, VALID_DIGIT_MAPPING[word], 1)
    return line


def calibrate_adjusted(line: str) -> int:
    """Spelled out digits now also count"""
    replaced_line = replace_words_with_digits(line)
    integers = [c for c in replaced_line if c.isdigit()]
    num_string = ""
    if not integers:
        num_string = 0
    elif len(integers) == 1:
        num_string = f'{integers[0]}{integers[0]}'
    else:
        num_string = f'{integers[0]}{integers[-1]}'
    return int(num_string)


def puzzle_two(raw_data: list) -> int:
    """What is the sum of all of the adjusted calibration values?"""
    values = [calibrate_adjusted(x) for x in raw_data]
    return sum(values)


if __name__ == "__main__":
    raw_data = get_file_contents(INPUT_FILE)

    result = puzzle_one(raw_data)
    plog(result)

    result = puzzle_two(raw_data)
    plog(result)
