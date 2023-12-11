from days.day05 import create_map

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
