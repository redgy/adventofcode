from days.day03 import create_matrix, is_symbol, is_out_of_bounds, is_adjacent_to_symbol, \
    get_number, get_adjacent_part_numbers
from copy import deepcopy


def create_mock_matrix(string_list):
    return [list(x) for x in string_list]


class TestCreateMatrix:
    def test_init(self):
        mock_data = create_mock_matrix(['abc', 'def', 'ghi'])
        expected = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]
        actual = create_matrix(mock_data)
        assert actual == expected


class TestIsSymbol:
    def test_false(self):
        not_symbols = [
            '.',  # period
            'a',  # lowercase
            'A',  # uppercase
            '1'  # number
        ]
        expected = False
        for character in not_symbols:
            actual = is_symbol(character)
            assert actual == expected

    def test_true(self):
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '=', '_']
        expected = True
        for character in symbols:
            actual = is_symbol(character)
            assert actual == expected


class TestIsOutOfBounds:
    mock_matrix = create_mock_matrix([
        'redgy',
        'Redgy',
        'REDGY'
    ])

    def test_true__less_than_zero(self):
        row = -1
        col = -1
        mock_data = deepcopy(self.mock_matrix)
        actual = is_out_of_bounds(row, col, mock_data)
        expected = True
        assert actual == expected

    def test_true__more_than_length(self):
        row = 5
        col = 5
        mock_data = deepcopy(self.mock_matrix)
        actual = is_out_of_bounds(row, col, mock_data)
        expected = True
        assert actual == expected

    def test_false__in_bounds(self):
        row = 2
        col = 2
        mock_data = deepcopy(self.mock_matrix)
        actual = is_out_of_bounds(row, col, mock_data)
        expected = False
        assert actual == expected


class TestIsAdjacentToSymbol:
    mock_data = create_mock_matrix([
        '!%^&*',
        '!bbb*',
        '!ccc*',
        '!ddd*',
        '!@#$*',
        'eeeee',
        'fffff'
    ])

    def test_true__left(self):
        row = 1
        col = 1
        actual = is_adjacent_to_symbol(row, col, self.mock_data)
        expected = True
        assert actual == expected

    def test_true__up(self):
        row = 1
        col = 2
        actual = is_adjacent_to_symbol(row, col, self.mock_data)
        expected = True
        assert actual == expected

    def test_true__right(self):
        row = 1
        col = 3
        actual = is_adjacent_to_symbol(row, col, self.mock_data)
        expected = True
        assert actual == expected

    def test_true__down(self):
        row = 3
        col = 2
        actual = is_adjacent_to_symbol(row, col, self.mock_data)
        expected = True
        assert actual == expected

    def test_true__diagonal__up_left(self):
        row = 1
        col = 1
        actual = is_adjacent_to_symbol(row, col, self.mock_data)
        expected = True
        assert actual == expected

    def test_true__diagonal__up_right(self):
        row = 1
        col = 3
        actual = is_adjacent_to_symbol(row, col, self.mock_data)
        expected = True
        assert actual == expected

    def test_true__diagonal__down_left(self):
        row = 3
        col = 1
        actual = is_adjacent_to_symbol(row, col, self.mock_data)
        expected = True
        assert actual == expected

    def test_true__diagonal__down_right(self):
        row = 3
        col = 3
        actual = is_adjacent_to_symbol(row, col, self.mock_data)
        expected = True
        assert actual == expected

    def test_false__surrounded_by_non_symbols(self):
        row = 2
        col = 2
        actual = is_adjacent_to_symbol(row, col, self.mock_data)
        expected = False
        assert actual == expected

    def test_false__row_does_not_exist(self):
        row = 6
        col = 2
        actual = is_adjacent_to_symbol(row, col, self.mock_data)
        expected = False
        assert actual == expected

    def test_false__col_does_not_exist(self):
        row = 6
        col = -1
        actual = is_adjacent_to_symbol(row, col, self.mock_data)
        expected = False
        assert actual == expected


class TestGetNumber:
    def test_before_index(self):
        mock_data = '123...'
        mock_index = 3
        expected = 123
        actual = get_number(list(mock_data), mock_index)
        assert actual == expected

    def test_on_index__beginning(self):
        mock_data = '123...'
        mock_index = 0
        expected = 123
        actual = get_number(list(mock_data), mock_index)
        assert actual == expected

    def test_on_index__end(self):
        mock_data = '123...'
        mock_index = 2
        expected = 123
        actual = get_number(list(mock_data), mock_index)
        assert actual == expected

    def test_on_index__between(self):
        mock_data = '123...'
        mock_index = 1
        expected = 123
        actual = get_number(list(mock_data), mock_index)
        assert actual == expected

    def test_after_index(self):
        mock_data = '....123...'
        mock_index = 3
        expected = 123
        actual = get_number(list(mock_data), mock_index)
        assert actual == expected

    def test_two_numbers__first_number__beginning(self):
        mock_data = '123...456...'
        mock_index = 0
        expected = 123
        actual = get_number(list(mock_data), mock_index)
        assert actual == expected

    def test_two_numbers__first_number__middle(self):
        mock_data = '123...456...'
        mock_index = 1
        expected = 123
        actual = get_number(list(mock_data), mock_index)
        assert actual == expected

    def test_two_numbers__first_number__end(self):
        mock_data = '123...456...'
        mock_index = 2
        expected = 123
        actual = get_number(list(mock_data), mock_index)
        assert actual == expected

    def test_two_numbers__second_number__before(self):
        mock_data = '123...456...'
        mock_index = 5
        expected = 456
        actual = get_number(list(mock_data), mock_index)
        assert actual == expected

    def test_two_numbers__second_number__beginning(self):
        mock_data = '123...456...'
        mock_index = 6
        expected = 456
        actual = get_number(list(mock_data), mock_index)
        assert actual == expected

    def test_two_numbers__second_number__middle(self):
        mock_data = '123...456...'
        mock_index = 7
        expected = 456
        actual = get_number(list(mock_data), mock_index)
        assert actual == expected

    def test_two_numbers__second_number__end(self):
        mock_data = '123...456...'
        mock_index = 8
        expected = 456
        actual = get_number(list(mock_data), mock_index)
        assert actual == expected


class TestGetAdjacentPartNumbers:
    mock_data = create_mock_matrix([
        '14***',
        '*****',
        '***7*',
        '**152',
        '*****',
        '***9*',
        '*****',
    ])

    def test_zero__edge(self):
        row = 3
        col = 0
        actual = get_adjacent_part_numbers(row, col, self.mock_data)
        expected = []
        assert actual == expected

    def test_zero__center(self):
        row = 5
        col = 1
        actual = get_adjacent_part_numbers(row, col, self.mock_data)
        expected = []
        assert actual == expected

    def test_one__up__double_digit(self):
        row = 1
        col = 0
        actual = get_adjacent_part_numbers(row, col, self.mock_data)
        expected = [14]
        assert actual == expected
        row = 1
        col = 1
        actual = get_adjacent_part_numbers(row, col, self.mock_data)
        assert actual == expected

    def test_one__down_single_digit(self):
        row = 1
        col = 3
        actual = get_adjacent_part_numbers(row, col, self.mock_data)
        expected = [7]
        assert actual == expected

    def test_one__right(self):
        row = 3
        col = 1
        actual = get_adjacent_part_numbers(row, col, self.mock_data)
        expected = [152]
        assert actual == expected

    def test_one__left(self):
        row = 0
        col = 2
        actual = get_adjacent_part_numbers(row, col, self.mock_data)
        expected = [14]
        assert actual == expected

    def test_one__diagonal__left_up(self):
        row = 6
        col = 4
        actual = get_adjacent_part_numbers(row, col, self.mock_data)
        expected = [9]
        assert actual == expected

    def test_one__diagonal__right_up(self):
        row = 4
        col = 1
        actual = get_adjacent_part_numbers(row, col, self.mock_data)
        expected = [152]
        assert actual == expected

    def test_one__diagonal__left_down(self):
        row = 1
        col = 4
        actual = get_adjacent_part_numbers(row, col, self.mock_data)
        expected = [7]
        assert actual == expected

    def test_one__diagonal__right_down(self):
        row = 2
        col = 1
        actual = get_adjacent_part_numbers(row, col, self.mock_data)
        expected = [152]
        assert actual == expected

    def test_two(self):
        row = 2
        col = 2
        actual = get_adjacent_part_numbers(row, col, self.mock_data)
        expected = [7, 152]
        assert set(actual) == set(expected)
