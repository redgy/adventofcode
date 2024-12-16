from days.day02 import (
    is_all_increasing,
    is_all_decreasing,
    get_difference,
    is_safe,
    remove_one_unsafe_level
)


class TestIsAllIncreasing:
    def test_true__by_1(self):
        mock_data = [1, 2, 3, 4]
        expected = True
        actual = is_all_increasing(mock_data)
        assert actual == expected

    def test_true__by_2(self):
        mock_data = [1, 3, 5, 7]
        expected = True
        actual = is_all_increasing(mock_data)
        assert actual == expected

    def test_true__random(self):
        mock_data = [1, 13, 25, 77]
        expected = True
        actual = is_all_increasing(mock_data)
        assert actual == expected

    def test_false__same(self):
        mock_data = [1, 1, 1, 1]
        expected = False
        actual = is_all_increasing(mock_data)
        assert actual == expected

    def test_false__only_1(self):
        mock_data = [1, 11, 21, 1]
        expected = False
        actual = is_all_increasing(mock_data)
        assert actual == expected


class TestIsAllDecreasing:
    def test_true__by_1(self):
        mock_data = [4, 3, 2, 1]
        expected = True
        actual = is_all_decreasing(mock_data)
        assert actual == expected

    def test_true__by_2(self):
        mock_data = [7, 5, 3, 1]
        expected = True
        actual = is_all_decreasing(mock_data)
        assert actual == expected

    def test_true__random(self):
        mock_data = [888, 214, 86, 0]
        expected = True
        actual = is_all_decreasing(mock_data)
        assert actual == expected

    def test_false__same(self):
        mock_data = [1, 1, 1, 1]
        expected = False
        actual = is_all_decreasing(mock_data)
        assert actual == expected

    def test_false__only_1(self):
        mock_data = [71, 61, 21, 31]
        expected = False
        actual = is_all_decreasing(mock_data)
        assert actual == expected


class TestGetDifference:
    def test_positive(self):
        expected = 7-1
        actual = get_difference(1, 7)
        assert actual == expected

    def test_negative_returns_positive(self):
        expected = 10-7
        actual = get_difference(10, 7)
        assert actual == expected

    def test_zero(self):
        expected = 10-10
        actual = get_difference(10, 10)
        assert actual == expected


class TestIsSafe:
    def test_false__not_all_increasing(self):
        mock_data = [1, 2, 3, 1]
        expected = False
        actual = is_safe(mock_data)
        assert actual == expected

    def test_false__not_all_decreasing(self):
        mock_data = [3, 2, 1, 11]
        expected = False
        actual = is_safe(mock_data)
        assert actual == expected

    def test_false__differ_less_than_one(self):
        mock_data = [3, 2, 1, 1]
        expected = False
        actual = is_safe(mock_data)
        assert actual == expected

    def test_false__differ_more_than_three(self):
        mock_data = [1, 3, 10, 13]
        expected = False
        actual = is_safe(mock_data)
        assert actual == expected

    def test_true__all_increasing__by_one(self):
        mock_data = [1, 2, 3, 4]
        expected = True
        actual = is_safe(mock_data)
        assert actual == expected

    def test_true__all_increasing__by_two(self):
        mock_data = [1, 3, 5, 7]
        expected = True
        actual = is_safe(mock_data)
        assert actual == expected

    def test_true__all_increasing__by_three(self):
        mock_data = [1, 4, 7, 10]
        expected = True
        actual = is_safe(mock_data)
        assert actual == expected

    def test_true__all_decreasing__by_one(self):
        mock_data = [4, 3, 2, 1]
        expected = True
        actual = is_safe(mock_data)
        assert actual == expected

    def test_true__all_decreasing__by_two(self):
        mock_data = [8, 6, 4, 2]
        expected = True
        actual = is_safe(mock_data)
        assert actual == expected

    def test_true__all_decreasing__by_three(self):
        mock_data = [11, 8, 5, 2]
        expected = True
        actual = is_safe(mock_data)
        assert actual == expected


class TestRemoveOneUnsafeLevel:
    expected_increase_data = [1, 2, 3]
    expected_decrease_data = [3, 2, 1]

    def test_increasing__first_pair__same(self):
        mock_data = [1, 1, 2, 3]
        expected = self.expected_increase_data
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected

    def test_increasing__first_pair__not_same(self):
        mock_data = [3, 1, 2, 3]
        expected = self.expected_increase_data
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected

    def test_increasing__last_pair__same(self):
        mock_data = [1, 2, 3, 3]
        expected = self.expected_increase_data
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected

    def test_increasing__last_pair__not_same(self):
        mock_data = [1, 2, 3, 1]
        expected = self.expected_increase_data
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected

    def test_increasing__middle_pair__same(self):
        mock_data = [1, 2, 2, 3]
        expected = self.expected_increase_data
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected

    def test_increasing__middle_pair__not_same(self):
        mock_data = [1, 3, 2, 3]
        expected = self.expected_increase_data
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected

    def test_decreasing__first_pair__same(self):
        mock_data = [3, 3, 2, 1]
        expected = self.expected_decrease_data
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected

    def test_decreasing__first_pair__not_same(self):
        mock_data = [1, 3, 2, 1]
        expected = self.expected_decrease_data
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected

    def test_decreasing__last_pair__same(self):
        mock_data = [3, 2, 1, 1]
        expected = self.expected_decrease_data
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected

    def test_decreasing__last_pair__not_same(self):
        mock_data = [3, 2, 1, 7]
        expected = self.expected_decrease_data
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected

    def test_decreasing__middle_pair__same(self):
        mock_data = [3, 2, 2, 1]
        expected = self.expected_decrease_data
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected

    def test_decreasing__middle_pair__not_same__first_num(self):
        mock_data = [3, 7, 2, 1]
        expected = self.expected_decrease_data
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected

    def test_decreasing__middle_pair__not_same__second_num(self):
        mock_data = [3, 2, 7, 1]
        expected = self.expected_decrease_data
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected

    def test_difference__first_pair__increasing(self):
        mock_data = [1, 5, 6, 7]
        expected = [5, 6, 7]
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected

    def test_difference__first_pair__decreasing(self):
        mock_data = [5, 1, 0]
        expected = [1, 0]
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected

    def test_difference__last_pair__increasing(self):
        mock_data = [1, 2, 3, 7]
        expected = [1, 2, 3]
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected

    def test_difference__last_pair__decreasing(self):
        mock_data = [8, 6, 1]
        expected = [8, 6]
        actual = remove_one_unsafe_level(mock_data)
        assert actual == expected
