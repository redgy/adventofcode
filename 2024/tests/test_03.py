from days.day03 import (
    get_all_mul_start_paren_indexes,
    get_all_dont_indexes,
    get_all_do_indexes,
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


class TestGetAllDontIndexes:
    def test_no_donts__empty(self):
        mock_input = ''
        expected = []
        actual = get_all_dont_indexes(mock_input)
        assert actual == expected

    def test_no_donts__non_empty(self):
        mock_input = 'i am not empty'
        expected = []
        actual = get_all_dont_indexes(mock_input)
        assert actual == expected

    def test_missing_parens(self):
        mock_input = 'dont'
        expected = []
        actual = get_all_dont_indexes(mock_input)
        assert actual == expected

    def test_missing_open_parens(self):
        mock_input = 'dont)'
        expected = []
        actual = get_all_dont_indexes(mock_input)
        assert actual == expected

    def test_missing_closing_parens(self):
        mock_input = 'dont('
        expected = []
        actual = get_all_dont_indexes(mock_input)
        assert actual == expected

    def test_found__one(self):
        mock_input = 'dont()'
        expected = [0]
        actual = get_all_dont_indexes(mock_input)
        assert actual == expected

    def test_found__two__back_to_back(self):
        mock_input = 'dont()dont()'
        expected = [0, 6]
        actual = get_all_dont_indexes(mock_input)
        assert actual == expected

    def test_found__two__in_between(self):
        mock_input = 'dont();somerthing;asdfdont()'
        expected = [0, 22]
        actual = get_all_dont_indexes(mock_input)
        assert actual == expected


class TestGetAllDoIndexes:
    def test_no_dos__empty(self):
        mock_input = ''
        expected = []
        actual = get_all_do_indexes(mock_input)
        assert actual == expected

    def test_no_dos__non_empty(self):
        mock_input = 'i am not empty'
        expected = []
        actual = get_all_do_indexes(mock_input)
        assert actual == expected

    def test_missing_parens(self):
        mock_input = 'do'
        expected = []
        actual = get_all_do_indexes(mock_input)
        assert actual == expected

    def test_missing_open_parens(self):
        mock_input = 'do)'
        expected = []
        actual = get_all_do_indexes(mock_input)
        assert actual == expected

    def test_missing_closing_parens(self):
        mock_input = 'do('
        expected = []
        actual = get_all_do_indexes(mock_input)
        assert actual == expected

    def test_found__one(self):
        mock_input = 'do()'
        expected = [0]
        actual = get_all_do_indexes(mock_input)
        assert actual == expected

    def test_found__two__back_to_back(self):
        mock_input = 'do()do()'
        expected = [0, 4]
        actual = get_all_do_indexes(mock_input)
        assert actual == expected

    def test_found__two__in_between(self):
        mock_input = 'do();somerthing;asdfdo()'
        expected = [0, 20]
        actual = get_all_do_indexes(mock_input)
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
