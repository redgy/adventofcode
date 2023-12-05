from days.day01 import calibrate, calibrate_adjusted


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
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_no_digits(self):
        expected = 0
        mock_string = 'abc'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_two_digits_in_between(self):
        expected = 34
        mock_string = 'a3b4c'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_three_digits_in_between(self):
        expected = 35
        mock_string = 'a3b4c5d'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_one_digit(self):
        expected = 99
        mock_string = 'abc9def'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_one_digit_is_zero__first(self):
        expected = 1
        mock_string = '0abc1'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_one_digit_is_zero__last(self):
        expected = 80
        mock_string = '8abc0'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_num_str_on_both_ends__digit_between(self):
        expected = 29
        mock_string = 'two1nine'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_num_str_on_both_ends__num_str_between(self):
        expected = 83
        mock_string = 'eighttwothree'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_num_str_in_between(self):
        expected = 13
        mock_string = 'abcone2threexyz'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_num_str_bleeds_into_other_number(self):
        expected = 24
        mock_string = 'xtwone3four'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_num_str_overlaps__oneight(self):
        expected = 18
        mock_string = 'oneight'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_num_str_overlaps__threeight(self):
        expected = 38
        mock_string = 'threeight'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_num_str_overlaps__fiveight(self):
        expected = 58
        mock_string = 'fiveight'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_num_str_overlaps__nineight(self):
        expected = 98
        mock_string = 'nineight'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_num_str_overlaps__twone(self):
        expected = 21
        mock_string = 'twone'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_num_str_overlaps__sevenine(self):
        expected = 79
        mock_string = 'sevenine'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_num_str_overlaps__eightwo(self):
        expected = 82
        mock_string = 'eightwo'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_num_str_overlaps__eighthree(self):
        expected = 83
        mock_string = 'eighthree'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_num_str_overlaps__starts_with_digit(self):
        expected = 13
        mock_string = '1eighthree'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_num_str_and_digit(self):
        expected = 14
        mock_string = 'zoneight234'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected

    def test_digit_and_num_str(self):
        expected = 76
        mock_string = '7pqrstsixteen'
        actual = calibrate_adjusted(mock_string)
        assert actual == expected
