# DAY 03 -- MULL IT OVER
from read_file import read_txt


SAMPLE = 'samples/day03.txt'
INPUT = 'input/day03.txt'


def get_all_mul_indexes(line: str) -> list[int]:
    """From line, get all starting indexes of "mul("""
    pass


def is_valid_instruction(line: str) -> bool:
    """Checks instruction that lives between parentheses is valid

    e.g. Input will be `mul(THIS_INSTRUCTION_BETWEEN_PARENTHESES)`
    """
    pass


def parse_instruction(line: str) -> tuple[int, int] | None:
    """Parses the string to get the instruction

    :param str line: Should be everything that follows `mul(`
    :returns: If valid instruction, releases tuple of ints
              Else None
    """
    pass


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
