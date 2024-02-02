from days.day09 import calculate_step, get_step_array, fill_extrapolated_values, get_extrapolated_values


class TestCalculateStep:
    def test_nonzero__positive(self):
        num1 = 7
        num2 = 9
        expected = num2 - num1
        actual = calculate_step(num1, num2)
        assert actual == expected

    def test_nonzero__negative(self):
        num1 = 10
        num2 = 5
        expected = num2 - num1
        actual = calculate_step(num1, num2)
        assert actual == expected

    def test_zero(self):
        num1 = 2
        num2 = 2
        expected = 0
        actual = calculate_step(num1, num2)
        assert actual == expected


class TestGetStepArray:
    def test_nonzero(self):
        expected = [1 for x in range(4)]
        mock_data = [x for x in range(5)].reverse()
        actual = get_step_array(mock_data)
        assert actual == expected

    def test_all_zero(self):
        expected = [0 for x in range(4)]
        mock_data = [1 for x in range(5)]
        actual = get_step_array(mock_data)
        assert actual == expected


class TestFillExtrapolatedValues:
    def test_two_steps(self):
        mock_data = [
            [0, 3, 6, 9, 12, 15],
            [3, 3, 3, 3, 3],
            [0, 0, 0, 0]
        ]
        expected = [
            [0, 3, 6, 9, 12, 15, 18],
            [3, 3, 3, 3, 3, 3],
            [0, 0, 0, 0, 0]
        ]
        actual = fill_extrapolated_values(mock_data)
        assert actual == expected

    def test_three_steps(self):
        mock_data = [
            [1, 3, 6, 10, 15, 21],
            [2, 3, 4, 5, 6],
            [1, 1, 1, 1],
            [0, 0, 0]
        ]
        expected = [
            [0, 3, 6, 9, 12, 15, 18],
            [3, 3, 3, 3, 3, 3],
            [0, 0, 0, 0, 0]
        ]
        actual = fill_extrapolated_values(mock_data)
        assert actual == expected

    def test_five_steps(self):
        mock_data = [
            [10, 13, 16, 21, 30, 45],
            [3, 3, 5, 9, 15],
            [2, 2, 2],
            [0, 0]
        ]
        expected = [
            [10, 13, 16, 21, 30, 45, 68],
            [3, 3, 5, 9, 15, 23],
            [2, 2, 2, 2],
            [0, 0, 0]
        ]
        actual = fill_extrapolated_values(mock_data)
        assert actual == expected


class TestGetExtrapolatedValues:
    def test_get_values(self):
        mock_data = [
            [10, 13, 16, 21, 30, 45, 68],
            [3, 3, 5, 9, 15, 23],
            [2, 2, 2, 2],
            [0, 0, 0]
        ]
        expected = [68, 23, 2, 0]
        actual = get_extrapolated_values(mock_data)
        assert actual == expected
