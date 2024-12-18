# DAY 03 -- MULL IT OVER
from read_file import read_txt
import re


SAMPLE = 'samples/day03.txt'
SAMPLE2 = 'samples/day03b.txt'
INPUT = 'input/day03.txt'
MUL_EXPR = re.compile(r'mul\(')
DONT_EXPR = re.compile(r'don\'t\(\)')
DO_EXPR = re.compile(r'do\(\)')


def get_all_mul_start_paren_indexes(line: str) -> list[int]:
    """From line, get all indexes of beginning paren of 'mul(' """
    matches = re.finditer(r'mul\(', line)
    return [match_obj.end() for match_obj in matches]


def get_all_dont_indexes(line: str) -> list[int]:
    """Get all starting indexes of dont()"""
    matches = re.finditer(r'don\'t\(\)', line)
    return [match_obj.start() for match_obj in matches]


def get_all_do_indexes(line: str) -> list[int]:
    """Get all starting indexes of do()"""
    matches = re.finditer(r'do\(\)', line)
    return [match_obj.start() for match_obj in matches]


def get_starting_index(mul_index: int, dont_index: int, do_index: int) -> tuple[int, int]:
    if mul_index is None:
        mul_index = -1
    if dont_index is None:
        dont_index = -1
    if do_index is None:
        do_index = -1
    all_indexes = [mul_index, dont_index, do_index]
    max_index = max(all_indexes) + 1
    for i, index in enumerate(all_indexes):
        if index == -1:
            all_indexes[i] = max_index
    min_index = min(all_indexes)
    for i, index in enumerate(all_indexes):
        if index == min_index:
            return i, index
    return None, None


def is_valid_instruction(line: str) -> bool:
    """Checks instruction that lives between parentheses is valid

    e.g. Input will be what exists between parentheses `mul(THIS_INSTRUCTION_BETWEEN_PARENTHESES)`
    """
    result = re.fullmatch(r'\d+,\d+', line)
    return result is not None


def parse_instruction(line: str) -> tuple[int, int] | None:
    """Parses the string to get the instruction

    :param str line: Should be the text after the first parentheses
    :returns: If valid instruction, releases tuple of ints
              Else None
    """
    end_paren_index = line.find(')')
    instruction = line[:end_paren_index]
    if is_valid_instruction(instruction):
        one, two = instruction.split(',')
        return int(one), int(two)
    return None, None


def part_one(data):
    results = []
    for line in data:
        start_paren_matches = get_all_mul_start_paren_indexes(line)
        for index in start_paren_matches:
            one, two = parse_instruction(line[index:])
            if one and two:
                results.append(one*two)
    return sum(results)


def _get_index(match_obj):
    if match_obj:
        return match_obj.end()
    return -1


def find_indexes(line):
    mul_index = _get_index(MUL_EXPR.search(line))
    dont_index = _get_index(DONT_EXPR.search(line))
    do_index = _get_index(DO_EXPR.search(line))
    zero_one_or_two, min_index = get_starting_index(mul_index, dont_index, do_index)
    return zero_one_or_two, min_index


def parse_line(line: str):
    results = []
    is_enabled = True
    curr_index = 0
    curr_line = line
    while curr_index < len(line):
        zero_one_or_two, min_index = find_indexes(curr_line)
        curr_index += min_index + 1
        match zero_one_or_two:
            case 0:
                if is_enabled:
                    num_one, num_two = parse_instruction(curr_line[min_index:])
                    if num_one and num_two:
                        results.append(num_one * num_two)
            case 1:
                is_enabled = False
            case _:
                is_enabled = True
        curr_line = curr_line[min_index+1:]
    return results


def part_two(data):
    results = []
    for line in data:
        results.extend(parse_line(line))
    return sum(results)


def main():
    sample_raw_data = read_txt(SAMPLE)
    input_raw_data = read_txt(INPUT)

    sample_result = part_one(sample_raw_data)
    print(f'Sample result part one: {sample_result}')
    input_result = part_one(input_raw_data)
    print(f'Input result part one: {input_result}')

    sample_raw_data = read_txt(SAMPLE2)
    sample_result = part_two(sample_raw_data)
    print(f'Sample result part two: {sample_result}')
    input_result = part_two(input_raw_data)
    print(f'Input result part two: {input_result}')


if __name__ == '__main__':
    main()
