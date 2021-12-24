INPUT_FILEPATH="day05_input.txt"
INPUT_FILEPATH="test_input.txt"
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


class Grid:
    def __init__(self, lines):
        self.lines = lines
        self.max = self._determine_max()
        self.grid = [['.' for x in range(self.max)] for x in range(self.max)]
        print(self)

    def __str__(self):
        to_string = ''
        for row in self.grid:
            for col in row:
                to_string += (f'{col}')
            to_string += ('\n')
        to_string += '-----------------------------------'
        return to_string

    def _determine_max(self):
        curr_max = 1
        for line in self.lines:
            curr_max = self._compare_max(curr_max, line.start)
            curr_max = self._compare_max(curr_max, line.end)
        return curr_max

    def _compare_max(self, curr_max, point):
        number = point.x if point.x > point.y else point.y
        return number if number > curr_max else curr_max

class Vents:
    def __init__(self, line_data):
        self.lines = []
        self.add_lines(line_data)
        self.grid = Grid(self.lines)

    def add_lines(self, line_data):
        for data in line_data:
            points_array = data.split(':')
            start_data = points_array[0].split(',')
            end_data = points_array[1].split(',')
            self.lines.append(Line(start_data, end_data))

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
