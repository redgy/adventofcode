from days.day01 import calibrate


class TestCalibrate:
    def test_digits_on_ends(self):
        expected = 12
        mock_string = '1abc2'
        actual = calibrate(mock_string)
        assert actual == expected

    def test_no_digits(self):
        expected = 0
        mock_string = 'abc'
        actual = calibrate(mock_string)
        assert actual == expected

    def test_two_digits_in_between(self):
        expected = 34
        mock_string = 'a3b4c'
        actual = calibrate(mock_string)
        assert actual == expected

    def test_three_digits_in_between(self):
        expected = 35
        mock_string = 'a3b4c5d'
        actual = calibrate(mock_string)
        assert actual == expected

    def test_one_digit(self):
        expected = 99
        mock_string = 'abc9def'
        actual = calibrate(mock_string)
        assert actual == expected

    def test_one_digit_is_zero__first(self):
        expected = 1
        mock_string = '0abc1'
        actual = calibrate(mock_string)
        assert actual == expected

    def test_one_digit_is_zero__last(self):
        expected = 80
        mock_string = '8abc0'
        actual = calibrate(mock_string)
        assert actual == expected
