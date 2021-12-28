INPUT_FILEPATH="day09_input.txt"
INPUT_FILEPATH="test_input.txt"
class Cell:
    def __init__(self, height, x, y, max_x, max_y):
        self.height = height
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y
        self.is_low_point = False
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self._init_adjacent_cells()

    def __str__(self):
        to_string = (f'[{self.x}, {self.y}]: {self.height}')
        if self.is_low_point:
            to_string += ' (L)'
        return to_string

    def set_is_low_point(self, new_value):
        self.is_low_point = new_value

    def get_adjacent_cells(self):
        adjacent_cells = []
        if self.left:
            adjacent_cells.append(self.left)
        if self.right:
            adjacent_cells.append(self.right)
        if self.up:
            adjacent_cells.append(self.up)
        if self.down:
            adjacent_cells.append(self.down)
        return adjacent_cells

    def set_left(self, x, y):
        self.left = (x, y) if self.is_cell_valid(x, y) else None

    def set_right(self, x, y):
        self.right = (x, y) if self.is_cell_valid(x, y) else None

    def set_up(self, x, y):
        self.up = (x, y) if self.is_cell_valid(x, y) else None

    def set_down(self, x, y):
        self.down = (x, y) if self.is_cell_valid(x, y) else None

    def _init_adjacent_cells(self):
        self.set_left(self.x, self.y-1)
        self.set_right(self.x, self.y+1)
        self.set_up(self.x-1, self.y)
        self.set_down(self.x+1, self.y)

    def is_cell_valid(self, x, y):
        is_x_valid = (x >=0 and x < self.max_x)
        is_y_valid = (y >= 0 and y < self.max_y)
        return is_x_valid and is_y_valid


class FloorMap:
    def __init__(self, row_data, num_lines):
        self.x_length = len(row_data[0])
        self.y_length = num_lines
        self.floor_map = [[None for x in range(self.x_length)] for x in range(self.y_length)]
        self._populate_floor_map(row_data)

    def _populate_floor_map(self, data):
        for row, row_list in enumerate(data):
            for col, value in enumerate(row_list):
                new_cell = Cell(value, row, col, self.x_length, self.y_length)
                self.floor_map[row][col] = new_cell

    def __str__(self):
        to_string = ''
        for row in self.floor_map:
            for col in row:
                if col is None:
                    col = '*'
                to_string += f'{col} '
            to_string += '\n'
        to_string += '------------------------------------------------------------------------'
        return to_string


class InputData:
    def __init__(self):
        self.raw_data = None
        self.row_data = None
        self.num_lines = 0
        self.input_data = []
        self._parse_file()

    def _parse_file(self):
        with open(INPUT_FILEPATH, 'r') as f:
            raw_data = f.readlines()
        self.raw_data = [x.strip() for x in raw_data]
        self.row_data = [list(x) for x in self.raw_data]
        for row in self.row_data:
            self.num_lines += 1


def main():
    data = InputData()
    floor_map = FloorMap(data.row_data, data.num_lines)
    to_string = floor_map
    print(to_string)


main()
