INPUT_FILEPATH="day05_input.txt"
# INPUT_FILEPATH="test_input.txt"
class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


class Line:
    def __init__(self, start_data, end_data):
        self.start = Point(start_data[0], start_data[1])
        self.end = Point(end_data[0], end_data[1])

    def __str__(self):
        return f'({self.start.x:>3}, {self.start.y:>3}), ({self.end.x:>3}, {self.end.y:>3})'

class Vents:
    def __init__(self, line_data):
        self.max = 0
        self.lines = []
        self.add_lines(line_data)

    def add_lines(self, line_data):
        for data in line_data:
            points_array = data.split(':')
            start_data = points_array[0].split(',')
            end_data = points_array[1].split(',')
            print(Line(start_data, end_data))

class InputData:
    def __init__(self):
        self.raw_data = None
        self.line_data = []
        self._parse_file()
        self._clean_line_data()

    def _parse_file(self):
        with open(INPUT_FILEPATH, 'r') as f:
            raw_data = f.readlines()
            raw_data = [x.strip() for x in raw_data]
        self.raw_data = raw_data

    def _clean_line_data(self):
        for line in self.raw_data:
            clean_data = line.replace(' -> ', ':')
            self.line_data.append(clean_data)


def main():
    data = InputData()
    vents = Vents(data.line_data)


main()
