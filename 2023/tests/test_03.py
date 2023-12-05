from days.day03 import create_matrix, is_symbol, is_adjacent_to_symbol, is_part_number
from copy import deepcopy


class TestCreateMatrix:
    def test_init(self):
        mock_data = [
            'abc',
            'def',
            'ghi'
        ]
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
            '1',  # number
            2  # digit
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


class TestIsAdjacentToSymbol:
    def test_init(self):
        pass


class TestIsPartNumber:
    def test_init(self):
        pass
