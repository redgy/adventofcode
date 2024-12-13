from days.day01 import calculate_distance, get_min_pair
import pytest


class TestCalculateDistance:
    def test_same(self):
        mock_a = 1
        mock_b = 1
        expected = mock_b - mock_a
        actual = calculate_distance(mock_a, mock_b)
        assert actual == expected

    def test_a_bigger_than_b(self):
        mock_a = 10
        mock_b = 1
        expected = (mock_b - mock_a) * -1
        actual = calculate_distance(mock_a, mock_b)
        assert actual == expected

    def test_b_bigger_than_a(self):
        mock_a = 1
        mock_b = 10
        expected = mock_b - mock_a
        actual = calculate_distance(mock_a, mock_b)
        assert actual == expected


class TestGetMinPair:
    def test_same_list__same_order(self):
        mock_one = [1, 2, 3, 4]
        mock_two = [1, 2, 3, 4]
        expected = (1, 1)
        actual = get_min_pair(mock_one, mock_two)
        assert actual == expected

    def test_same_list__different_order(self):
        mock_one = [1, 2, 3, 4]
        mock_two = [2, 4, 1, 3]
        expected = (1, 1)
        actual = get_min_pair(mock_one, mock_two)
        assert actual == expected

    def test_different_lists(self):
        mock_one = [1, 2, 3, 4]
        mock_two = [5, 6, 7, 8]
        expected = (1, 5)
        actual = get_min_pair(mock_one, mock_two)
        assert actual == expected

    def test_error__different_lengths(self):
        mock_one = [1, 2, 3, 4]
        mock_two = [5, 6, 7]
        expected_error = 'list lengths are different'
        with pytest.raises(ValueError, match=expected_error):
            get_min_pair(mock_one, mock_two)
