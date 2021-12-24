INPUT_FILEPATH="day05_input.txt"
# INPUT_FILEPATH="test_input.txt"
class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other_point):
        if(isinstance(other_point, Point)):
            return self.x == other_point.x and self.y == other_point.y
        return false

    def calculate_midpoint(self, other_point):
        x = (self.x + other_point.x) / 2
        y = (self.y + other_point.y) / 2
        return Point(x, y)


class Line:
    def __init__(self, start_data, end_data):
        self.start = Point(start_data[0], start_data[1])
        self.end = Point(end_data[0], end_data[1])
        self.is_vertical = self.start.x == self.end.x
        self.is_horizontal = self.start.y == self.end.y
        self.x_diff = abs(self.start.x - self.end.x) + 1
        self.y_diff = abs(self.start.y - self.end.y) + 1
        self.midpoint = self.get_midpoint()

    def __str__(self):
        return f'({self.start.x:>3}, {self.start.y:>3}), ({self.end.x:>3}, {self.end.y:>3})'

    def get_midpoint(self):
        return self.start.calculate_midpoint(self.end)


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
            self.mark_line(line)

    def mark_line(self, line):
        if line.is_horizontal or line.is_vertical:
            self.update_cell(line.start.x, line.start.y)
            self.update_cell(line.end.x, line.end.y)
            self.mark_midpoint(line.start, line.midpoint, line.end)

    def mark_midpoint(self, start, midpoint, end):
        if midpoint == start or midpoint == end:
            return
        self.update_cell(midpoint.x, midpoint.y)

        left_midpoint = start.calculate_midpoint(midpoint)
        self.mark_midpoint(start, left_midpoint, midpoint)

        right_midpoint = midpoint.calculate_midpoint(end)
        self.mark_midpoint(midpoint, right_midpoint, end)

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
    # print(vents.grid)
    print(f'Found {number_of_danger_points} danger points')


main()
