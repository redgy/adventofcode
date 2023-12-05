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


class TestCalibrateAdjusted:
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

    def test_num_str_on_both_ends__digit_between(self):
        expected = 29
        mock_string = 'two1nine'
        actual = calibrate(mock_string)
        assert actual == expected

    def test_num_str_on_both_ends__num_str_between(self):
        expected = 83
        mock_string = 'eighttwothree'
        actual = calibrate(mock_string)
        assert actual == expected

    def test_num_str_in_between(self):
        expected = 13
        mock_string = 'abcone2threexyz'
        actual = calibrate(mock_string)
        assert actual == expected

    def test_num_str_bleeds_into_other_number(self):
        expected = 13
        mock_string = 'xtwone3four'
        actual = calibrate(mock_string)
        assert actual == expected

    def test_num_str_and_digit(self):
        expected = 14
        mock_string = 'zoneight234'
        actual = calibrate(mock_string)
        assert actual == expected

    def test_digit_and_num_str(self):
        expected = 14
        mock_string = '7pqrstsixteen'
        actual = calibrate(mock_string)
        assert actual == expected
