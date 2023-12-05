from utils import get_file_contents


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
