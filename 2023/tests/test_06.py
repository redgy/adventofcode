from days.day06 import calculate_distance


class TestCalculateDistance:
    def test_zero(self):
        expected = 0
        assert expected == calculate_distance(0, 7)
        assert expected == calculate_distance(7, 7)

    def test_six(self):
        expected = 6
        assert expected == calculate_distance(1, 7)
        assert expected == calculate_distance(6, 7)

    def test_ten(self):
        expected = 10
        assert expected == calculate_distance(2, 7)
        assert expected == calculate_distance(5, 7)

    def test_twelve(self):
        expected = 12
        assert expected == calculate_distance(3, 7)
        assert expected == calculate_distance(4, 7)
