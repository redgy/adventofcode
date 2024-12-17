from days.day03 import (
    get_all_mul_indexes,
    is_valid_instruction,
    parse_instruction
)


class TestGetAllMulIndexes:
    def test_all_valid(self):
        mock_input = ''
        expected = ''
        actual = get_all_mul_indexes(mock_input)
        assert actual == expected


class TestIsValidInstruction:
    def test_valid(self):
        mock_input = ''
        expected = ''
        actual = is_valid_instruction(mock_input)
        assert actual == expected


class TestParseInstruction:
    def test_valid(self):
        mock_input = ''
        expected = ''
        actual = parse_instruction(mock_input)
        assert actual == expected
