from days.day07 import get_hand_type, compare_hands


class TestHandType:
    def test_five_of_a_kind(self):
        mock_hand = '55555'
        actual = get_hand_type(mock_hand)
        expected = 7
        assert actual == expected

    def test_four_of_a_kind(self):
        mock_hand = '4444T'
        actual = get_hand_type(mock_hand)
        expected = 6
        assert actual == expected

    def test_full_house(self):
        mock_hand = 'KKKAA'
        actual = get_hand_type(mock_hand)
        expected = 5
        assert actual == expected

    def test_three_of_a_kind(self):
        mock_hand = '2J3JJ'
        actual = get_hand_type(mock_hand)
        expected = 4
        assert actual == expected

    def test_two_pair(self):
        mock_hand = 'QTQT9'
        actual = get_hand_type(mock_hand)
        expected = 3
        assert actual == expected

    def test_one_pair(self):
        mock_hand = '88123'
        actual = get_hand_type(mock_hand)
        expected = 2
        assert actual == expected

    def test_high_card(self):
        mock_hand = 'AKQJT'
        actual = get_hand_type(mock_hand)
        expected = 1
        assert actual == expected


class TestCompareHands:
    def test_first_card(self):
        mock_one = '53343'
        mock_two = '72228'
        actual = compare_hands(mock_one, mock_two)
        expected = mock_two
        assert actual == expected

    def test_second_card(self):
        mock_one = 'A9999'
        mock_two = 'AA876'
        actual = compare_hands(mock_one, mock_two)
        expected = mock_two
        assert actual == expected

    def test_third_card(self):
        mock_one = '435JT'
        mock_two = '43TTJ'
        actual = compare_hands(mock_one, mock_two)
        expected = mock_two
        assert actual == expected

    def test_fourth_card(self):
        mock_one = '992QK'
        mock_two = '992K7'
        actual = compare_hands(mock_one, mock_two)
        expected = mock_two
        assert actual == expected

    def test_fifth_card(self):
        mock_one = '34567'
        mock_two = '34568'
        actual = compare_hands(mock_one, mock_two)
        expected = mock_two
        assert actual == expected
