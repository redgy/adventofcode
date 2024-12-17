# DAY 03 -- MULL IT OVER
from read_file import read_txt
import re


SAMPLE = 'samples/day03.txt'
INPUT = 'input/day03.txt'


def get_all_mul_start_paren_indexes(line: str) -> list[int]:
    """From line, get all indexes of beginning paren of 'mul(' """
    matches = re.finditer(r'mul\(', line)
    return [match_obj.end() for match_obj in matches]


def is_valid_instruction(line: str) -> bool:
    """Checks instruction that lives between parentheses is valid

    e.g. Input will be what exists between parentheses `mul(THIS_INSTRUCTION_BETWEEN_PARENTHESES)`
    """
    result = re.fullmatch(r'\d+,\d+', line)
    return result is not None


def parse_instruction(line: str) -> tuple[int, int] | None:
    """Parses the string to get the instruction

    :param str line: Should be "mul(andwhatever is after the parentheses"
    :returns: If valid instruction, releases tuple of ints
              Else None
    """
    end_paren = line.find(')')
    print(end_paren)


def part_one(data):
    pass


def part_two(data):
    pass


def main():
    sample_raw_data = read_txt(SAMPLE)
    input_raw_data = read_txt(INPUT)

    sample_result = part_one(sample_raw_data)
    print(f'Sample result part one: {sample_result}')
    input_result = part_one(input_raw_data)
    print(f'Input result part one: {input_result}')

    sample_result = part_two(sample_raw_data)
    print(f'Sample result part two: {sample_result}')
    input_result = part_two(input_raw_data)
    print(f'Input result part two: {input_result}')


if __name__ == '__main__':
    main()
