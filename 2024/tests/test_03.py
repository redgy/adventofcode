from days.day03 import (
    get_all_mul_start_paren_indexes,
    is_valid_instruction,
    parse_instruction
)


class TestGetAllMulIndexes:
    def test_no_mul__empty(self):
        mock_input = ''
        expected = []
        actual = get_all_mul_start_paren_indexes(mock_input)
        assert actual == expected

    def test_no_mul__does_not_exist(self):
        mock_input = 'no m u l ()'
        expected = []
        actual = get_all_mul_start_paren_indexes(mock_input)
        assert actual == expected

    def test_one_mul(self):
        mock_input = 'mul()'
        expected = [4]
        actual = get_all_mul_start_paren_indexes(mock_input)
        assert actual == expected

    def test_multiple__back_to_back(self):
        mock_input = 'mul()mul()'
        expected = [4, 9]
        actual = get_all_mul_start_paren_indexes(mock_input)
        assert actual == expected

    def test_multiple__with_trash(self):
        mock_input = 'mul()thisbetrashmul()'
        expected = [4, 20]
        actual = get_all_mul_start_paren_indexes(mock_input)
        assert actual == expected


class TestIsValidInstruction:
    def test_valid(self):
        mock_input = '1111,11111'
        expected = True
        actual = is_valid_instruction(mock_input)
        assert actual == expected

    def test_invalid__not_numbers(self):
        mock_input = 'a,b'
        expected = False
        actual = is_valid_instruction(mock_input)
        assert actual == expected

    def test_invalid__trash(self):
        mock_input = 'this is a junkyard'
        expected = False
        actual = is_valid_instruction(mock_input)
        assert actual == expected

    def test_invalid__spaces(self):
        mock_input = ' 2222, 22222222'
        expected = False
        actual = is_valid_instruction(mock_input)
        assert actual == expected


class TestParseInstruction:
    def test_valid(self):
        mock_input = '1,2)'
        expected = (1, 2)
        actual = parse_instruction(mock_input)
        assert actual == expected

    def test_invalid__no_paren(self):
        mock_input = '1,2'
        expected = (None, None)
        actual = parse_instruction(mock_input)
        assert actual == expected

    def test_invalid__not_numbers(self):
        mock_input = 'a,b)'
        expected = (None, None)
        actual = parse_instruction(mock_input)
        assert actual == expected

    def test_invalid__trash(self):
        mock_input = 'dumpster fire'
        expected = (None, None)
        actual = parse_instruction(mock_input)
        assert actual == expected

    def test_invalid__spaces(self):
        mock_input = ' 1 , 2 )'
        expected = (None, None)
        actual = parse_instruction(mock_input)
        assert actual == expected
