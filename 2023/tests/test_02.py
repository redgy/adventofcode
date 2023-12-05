from days.day02 import get_max_game_data, is_game_possible, calculate_power
from copy import deepcopy


def create_game(red=None, blue=None, green=None):
    if not red and not blue and not green:
        return ''
    if not blue and not green:
        return f'{red} red'
    if not red and not green:
        return f'{blue} blue'
    if not red and not blue:
        return f'{green} green'
    if not red:
        return f'{blue} blue, {green} green'
    if not blue:
        return f'{red} red, {green} green'
    if not green:
        return f'{red} red, {blue} blue'
    return f'{red} red, {blue} blue, {green} green'


def create_record(id=17, games=[]):
    game_id = f'Game {id}'
    games_string = ';'.join(games)
    return f'{game_id}: {games_string}'


def create_game_dict(red=0, blue=0, green=0):
    return {
        'red': red,
        'blue': blue,
        'green': green,
    }


class TestGetMaxGameData:
    game_id = 333
    red = 10
    blue = 20
    green = 30

    def test_returns_data__all_colors__1_game(self):
        mock_games = [create_game(red=self.red, blue=self.blue, green=self.green)]
        mock_data = create_record(id=self.game_id, games=mock_games)
        actual = get_max_game_data(mock_data)
        expected = {
            self.game_id: {
                'red': self.red,
                'blue': self.blue,
                'green': self.green,
            }
        }
        assert actual == expected

    def test_returns_data__all_colors__2_games(self):
        mock_games = [
            create_game(red=self.red, blue=self.blue),
            create_game(green=self.green)
        ]
        mock_data = create_record(id=self.game_id, games=mock_games)
        actual = get_max_game_data(mock_data)
        expected = {
            self.game_id: {
                'red': self.red,
                'blue': self.blue,
                'green': self.green,
            }
        }
        assert actual == expected

    def test_returns_data__all_colors__3_games(self):
        mock_games = [
            create_game(red=self.red),
            create_game(blue=self.blue),
            create_game(green=self.green)
        ]
        mock_data = create_record(id=self.game_id, games=mock_games)
        actual = get_max_game_data(mock_data)
        expected = {
            self.game_id: {
                'red': self.red,
                'blue': self.blue,
                'green': self.green,
            }
        }
        assert actual == expected

    def test_returns_data__two_colors__no_red(self):
        mock_games = [
            create_game(blue=self.blue),
            create_game(green=self.green)
        ]
        mock_data = create_record(id=self.game_id, games=mock_games)
        actual = get_max_game_data(mock_data)
        expected = {
            self.game_id: {
                'red': 0,
                'blue': self.blue,
                'green': self.green,
            }
        }
        assert actual == expected

    def test_returns_data__two_colors__no_blue(self):
        mock_games = [
            create_game(red=self.red),
            create_game(green=self.green)
        ]
        mock_data = create_record(id=self.game_id, games=mock_games)
        actual = get_max_game_data(mock_data)
        expected = {
            self.game_id: {
                'red': self.red,
                'blue': 0,
                'green': self.green,
            }
        }
        assert actual == expected

    def test_returns_data__two_colors__no_green(self):
        mock_games = [
            create_game(red=self.red),
            create_game(blue=self.blue)
        ]
        mock_data = create_record(id=self.game_id, games=mock_games)
        actual = get_max_game_data(mock_data)
        expected = {
            self.game_id: {
                'red': self.red,
                'blue': self.blue,
                'green': 0,
            }
        }
        assert actual == expected

    def test_returns_data__one_color__red(self):
        mock_games = [create_game(red=self.red)]
        mock_data = create_record(id=self.game_id, games=mock_games)
        actual = get_max_game_data(mock_data)
        expected = {
            self.game_id: {
                'red': self.red,
                'blue': 0,
                'green': 0,
            }
        }
        assert actual == expected

    def test_returns_data__one_color__blue(self):
        mock_games = [create_game(blue=self.blue)]
        mock_data = create_record(id=self.game_id, games=mock_games)
        actual = get_max_game_data(mock_data)
        expected = {
            self.game_id: {
                'red': 0,
                'blue': self.blue,
                'green': 0,
            }
        }
        assert actual == expected

    def test_returns_data__one_color__green(self):
        mock_games = [create_game(green=self.green)]
        mock_data = create_record(id=self.game_id, games=mock_games)
        actual = get_max_game_data(mock_data)
        expected = {
            self.game_id: {
                'red': 0,
                'blue': 0,
                'green': self.green,
            }
        }
        assert actual == expected


class TestIsGamePossible:
    red = 99
    blue = 88
    green = 77
    max_data = create_game_dict(red=red, blue=blue, green=green)

    def test_true__same_max(self):
        mock_data = create_game_dict(red=self.red, blue=self.blue, green=self.green)
        expected = True
        actual = is_game_possible(mock_data, self.max_data)
        assert actual == expected

    def test_true__less_than_max(self):
        mock_data = create_game_dict(red=self.red-1, blue=self.blue-1, green=self.green-1)
        expected = True
        actual = is_game_possible(mock_data, self.max_data)
        assert actual == expected

    def test_false__more_than_max__non_zero(self):
        mock_data = create_game_dict(red=self.red, blue=self.blue, green=self.green)
        max_data = deepcopy(self.max_data)
        max_data['red'] -= 1
        expected = False
        actual = is_game_possible(mock_data, max_data)
        assert actual == expected

    def test_false__more_than_max__zero__red(self):
        mock_data = create_game_dict(red=self.red, blue=self.blue, green=self.green)
        max_data = deepcopy(self.max_data)
        max_data['red'] = 0
        expected = False
        actual = is_game_possible(mock_data, max_data)
        assert actual == expected

    def test_false__more_than_max__zero__blue(self):
        mock_data = create_game_dict(red=self.red, blue=self.blue, green=self.green)
        max_data = deepcopy(self.max_data)
        max_data['blue'] = 0
        expected = False
        actual = is_game_possible(mock_data, max_data)
        assert actual == expected

    def test_false__more_than_max__zero__green(self):
        mock_data = create_game_dict(red=self.red, blue=self.blue, green=self.green)
        max_data = deepcopy(self.max_data)
        max_data['green'] = 0
        expected = False
        actual = is_game_possible(mock_data, max_data)
        assert actual == expected


class TestCalculatePower:
    def test_returns_non_zero(self):
        red = 10
        blue = 20
        green = 30
        mock_data = create_game_dict(red=red, blue=blue, green=green)
        actual = calculate_power(mock_data)
        expected = red * blue * green
        assert actual == expected

    def test_returns_zero(self):
        red = 0
        blue = 20
        green = 30
        mock_data = create_game_dict(red=red, blue=blue, green=green)
        actual = calculate_power(mock_data)
        expected = 0
        assert actual == expected
