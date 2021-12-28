INPUT_FILEPATH="day09_input.txt"
INPUT_FILEPATH="test_input.txt"
class Cell:
    def __init__(self, x, y, height, left=None, right=None, up=None, down=None):
        self.x = x
        self.y = y
        self.height = height
        self.is_low_point = None
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def __str__(self):
        to_string = (f'[{self.x}, {self.y}]: {self.height}')
        if self.is_low_point:
            to_string += ' (L)'
        return to_string

    def is_low_point(self):
        is_low_point = True
        if self.is_low_point is None:
            adjacent_cells = self.get_adjacent_cells()
            for cell in adjacent_cells:
                if self.height > cell.height:
                    is_low_point = False
            self.is_low_point = is_low_point
        return self.is_low_point

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

    def set_left(self, cell):
        self.left = cell

    def set_right(self, cell):
        self.right = cell

    def set_up(self, cell):
        self.up = cell

    def set_down(self, cell):
        self.down = cell


class FloorMap:
    def __init__(self, row_data, num_lines):
        self.x_length = len(row_data[0])
        self.y_length = num_lines
        self.floor_map = [[None for x in range(self.x_length)] for x in range(self.y_length)]
        self._populate_floor_map(row_data)

    def _populate_floor_map(self, data):
        for row, row_list in enumerate(data):
            for col, value in enumerate(row_list):
                new_cell = Cell(row, col, value)
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
