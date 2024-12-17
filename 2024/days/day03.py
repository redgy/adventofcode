# DAY 03 -- MULL IT OVER
from read_file import read_txt
import re


SAMPLE = 'samples/day03.txt'
INPUT = 'input/day03.txt'


def get_all_mul_start_paren_indexes(line: str) -> list[int]:
    """From line, get all indexes of beginning paren of 'mul(' """
    matches = re.finditer(r'mul\(', line)
    return [match_obj.end() for match_obj in matches]


def get_all_dont_indexes(line: str) -> list[int]:
    """Get all starting indexes of dont()"""
    pass


def get_all_do_indexes(line: str) -> list[int]:
    """Get all starting indexes of do()"""
    pass


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


def part_two(data):
    pass


def main():
    sample_raw_data = read_txt(SAMPLE)
    input_raw_data = read_txt(INPUT)

    sample_result = part_one(sample_raw_data)
    print(f'Sample result part one: {sample_result}')
    input_result = part_one(input_raw_data)
    print(f'Input result part one: {input_result}')

    # sample_result = part_two(sample_raw_data)
    # print(f'Sample result part two: {sample_result}')
    # input_result = part_two(input_raw_data)
    # print(f'Input result part two: {input_result}')


if __name__ == '__main__':
    main()
