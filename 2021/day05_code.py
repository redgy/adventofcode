INPUT_FILEPATH="day05_input.txt"
class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


class Line:
    def __init__(self, start_data, end_data):
        self.start = Point(start_data[0], start_data[1])
        self.end = Point(end_data[0], end_data[1])
        self.is_vertical = self.start.x == self.end.x
        self.is_horizontal = self.start.y == self.end.y
        self.x_diff = abs(self.start.x - self.end.x) + 1
        self.y_diff = abs(self.start.y - self.end.y) + 1

    def __str__(self):
        return f'({self.start.x:>3}, {self.start.y:>3}), ({self.end.x:>3}, {self.end.y:>3})'


class Grid:
    def __init__(self, lines):
        self.lines = lines
        self.max = self._determine_max() + 1
        self.grid = [['.' for x in range(self.max)] for x in range(self.max)]

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

    def place_lines(self):
        for line in self.lines:
            is_valid = line.is_horizontal or line.is_vertical
            if is_valid:
                self.mark_line(line)

    def mark_line(self, line):
        if line.is_horizontal:
            if line.start.x < line.end.x:
                start_point = line.start
            else:
                start_point = line.end
            for x in range(line.x_diff):
                self.update_cell(start_point.x, start_point.y)
                start_point.x += 1
        elif line.is_vertical:
            if line.start.y < line.end.y:
                start_point = line.start
            else:
                start_point = line.end
            for y in range(line.y_diff):
                self.update_cell(start_point.x, start_point.y)
                start_point.y += 1

    def update_cell(self, x, y):
        cell_value = self.grid[x][y]
        cell_value = 1 if cell_value == '.' else cell_value +1
        self.grid[x][y] = cell_value

    def get_quantity(self, number):
        quantity = 0
        for row in self.grid:
            for col in row:
                value = 0 if col == '.' else col
                if value >= number:
                    quantity += 1
        return quantity


class Vents:
    def __init__(self, line_data):
        self.lines = []
        self._add_lines(line_data)
        self.grid = Grid(self.lines)

    def _add_lines(self, line_data):
        for data in line_data:
            points_array = data.split(':')
            start_data = points_array[0].split(',')
            end_data = points_array[1].split(',')
            self.lines.append(Line(start_data, end_data))

    def get_danger_areas(self):
        self.grid.place_lines()
        return self.grid.get_quantity(2)


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
    number_of_danger_points = vents.get_danger_areas()
    print(f'Found {number_of_danger_points} danger points')


main()
