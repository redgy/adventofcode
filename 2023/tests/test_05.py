from days.day05 import parse_data, create_map
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
