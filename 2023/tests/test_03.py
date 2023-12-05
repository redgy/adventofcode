from days.day03 import create_matrix, is_symbol, is_out_of_bounds, is_adjacent_to_symbol
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
        col = 0
        actual = is_adjacent_to_symbol(row, col, self.mock_data)
        expected = False
        assert actual == expected


class TestIsPartNumber:
    def test_init(self):
        pass
