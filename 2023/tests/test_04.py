from days.day04 import get_matching_winning_numbers, calculate_points


class TestMatchingWinningNumbers:
    mock_winning_numbers = [12, 34, 56, 78, 90]

    def test_no_matches__empty(self):
        expected = []
        mock_data = []
        actual = get_matching_winning_numbers(mock_data, self.mock_winning_numbers)
        assert actual == expected

    def test_no_matches(self):
        expected = []
        mock_data = [x for x in range(len(self.mock_winning_numbers))]
        actual = get_matching_winning_numbers(mock_data, self.mock_winning_numbers)
        assert actual == expected

    def test_matches__one(self):
        expected = self.mock_winning_numbers[:1]
        mock_data = expected + [x for x in range(len(self.mock_winning_numbers)-1)]
        actual = get_matching_winning_numbers(mock_data, self.mock_winning_numbers)
        assert actual == expected

    def test_matches__partial(self):
        expected = self.mock_winning_numbers[:2]
        mock_data = expected + [x for x in range(len(self.mock_winning_numbers) - len(expected))]
        actual = get_matching_winning_numbers(mock_data, self.mock_winning_numbers)
        assert set(actual) == set(expected)

    def test_matches__all(self):
        expected = self.mock_winning_numbers
        mock_data = expected
        actual = get_matching_winning_numbers(mock_data, self.mock_winning_numbers)
        assert set(actual) == set(expected)


class TestCalculatePoints:
    def test_zero(self):
        expected = 0
        mock_data = []
        actual = calculate_points(mock_data)
        assert actual == expected

    def test_one(self):
        expected = 1
        mock_data = [8]
        actual = calculate_points(mock_data)
        assert actual == expected

    def test_two(self):
        expected = 2
        mock_data = [22, 33]
        actual = calculate_points(mock_data)
        assert actual == expected

    def test_sixteen(self):
        expected = 16
        mock_data = [1, 2, 4, 8, 16]
        actual = calculate_points(mock_data)
        assert actual == expected
