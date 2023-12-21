from days.day05 import parse_data, create_map, get_location
from utils import get_file_contents


class TestParseData:
    raw_data = get_file_contents('samples/day05.txt')

    def test_keys(self):
        expected = [
            'seeds',
            'seed-to-soil',
            'soil-to-fertilizer',
            'fertilizer-to-water',
            'water-to-light',
            'light-to-temperature',
            'temperature-to-humidity',
            'humidity-to-location',
        ]
        actual = parse_data(self.raw_data)
        assert set(actual) == set(expected)


class TestCreateMap:
    def test_map(self):
        source_start = 10
        destination_start = 20
        range_length = 3
        expected = {
            source_start: destination_start,
            source_start+1: destination_start+1,
            source_start+2: destination_start+2,
        }
        actual = create_map(destination_start, source_start, range_length)
        assert actual == expected


class TestGetLocation:
    def test_has_set_number(self):
        mock_seed = 12
        expected = 34
        mock_almanac = {
            'seeds': mock_seed,
            'seed-to-soil': {mock_seed: 2},
            'soil-to-fertilizer': {2: 3},
            'fertilizer-to-water': {3: 4},
            'water-to-light': {4: 5},
            'light-to-temperature': {5: 6},
            'temperature-to-humidity': {6: 7},
            'humidity-to-location': {7: expected},
        }
        actual = get_location(mock_seed, mock_almanac)
        assert actual == expected
