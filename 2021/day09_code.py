INPUT_FILEPATH="day09_input.txt"
INPUT_FILEPATH="test_input.txt"
class Cell:
    def __init__(self, x, y, left=None, right=None, up=None, down=None):
        self.x = x
        self.y = y
        self.is_low_point = False
        self.left = left
        self.right = right
        self.up = up
        self.down = down


class FloorMap:
    def __init__(self, data):
        self.length = len(data[0])


class InputData:
    def __init__(self):
        self.raw_data = None
        self.input_data = []
        self._parse_file()

    def _parse_file(self):
        with open(INPUT_FILEPATH, 'r') as f:
            raw_data = f.readlines()
        self.raw_data = [x.strip() for x in raw_data]
        self.row_data = [list(x) for x in self.raw_data]


def main():
    data = InputData()


main()
