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
        self.risk_level = 0
        self.left_coords = None
        self.right_coords = None
        self.up_coords = None
        self.down_coords = None
        self._init_adjacent_cells()

    def __str__(self):
        to_string = (f'[{self.x}, {self.y}]: {self.height}')
        if self.is_low_point:
            to_string += ' (L)'
        return to_string

    def get_adjacent_cells_coords_list(self):
        adjacent_cells_coords_list = []
        if self.left_coords:
            adjacent_cells_coords_list.append(self.left_coords)
        if self.right_coords:
            adjacent_cells_coords_list.append(self.right_coords)
        if self.up_coords:
            adjacent_cells_coords_list.append(self.up_coords)
        if self.down_coords:
            adjacent_cells_coords_list.append(self.down_coords)
        return adjacent_cells_coords_list

    def set_left_coords(self, x, y):
        self.left_coords = (x, y) if self.is_cell_coords_valid(x, y) else None

    def set_right_coords(self, x, y):
        self.right_coords = (x, y) if self.is_cell_coords_valid(x, y) else None

    def set_up_coords(self, x, y):
        self.up_coords = (x, y) if self.is_cell_coords_valid(x, y) else None

    def set_down_coords(self, x, y):
        self.down_coords = (x, y) if self.is_cell_coords_valid(x, y) else None

    def _init_adjacent_cells(self):
        self.set_left_coords(self.x, self.y-1)
        self.set_right_coords(self.x, self.y+1)
        self.set_up_coords(self.x-1, self.y)
        self.set_down_coords(self.x+1, self.y)

    def is_cell_coords_valid(self, x, y):
        is_x_valid = (x >=0 and x < self.max_x)
        is_y_valid = (y >= 0 and y < self.max_y)
        return is_x_valid and is_y_valid


class FloorMap:
    def __init__(self, list_data, num_lines):
        single_row = list_data[0]
        self.num_cols = len(single_row)
        self.num_rows = num_lines
        self.floor_map = [[None for x in range(self.num_cols)] for x in range(self.num_rows)]
        self._populate_floor_map(list_data)

    def _populate_floor_map(self, data):
        for row, row_list in enumerate(data):
            for col, value in enumerate(row_list):
                new_cell = Cell(value, row, col, self.num_rows, self.num_cols)
                self.floor_map[row][col] = new_cell

    def set_low_points(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                current_cell = self.floor_map[row][col]
                self._set_cells_low_point(current_cell)

    def _set_cells_low_point(self, cell):
        adjacent_cell_coords = cell.get_adjacent_cell_coords()
        is_min = True
        for adjacent_cell in adjacent_cell_coords:
            if self._is_other_cell_lower(cell.height, adjacent_cell.height):
                is_min = False
        # is_left_lower = self._is_other_cell_lower(cell.height, cell.left)
        # is_right_lower = self._is_other_cell_lower(cell.height, cell.right)
        # is_up_lower = self._is_other_cell_lower(cell.height, cell.up)
        # is_down_lower = self._is_other_cell_lower(cell.height, cell.down)
        # is_min = (not is_left_lower and not is_right_lower and not is_up_lower and not is_down_lower)
        if is_min:
            print(cell)

    def _is_other_cell_lower(self, height, cell_tuple):
        if cell_tuple:
            row = cell_tuple[0]
            col = cell_tuple[1]
            other_height = self.floor_map[row][col].height
            if other_height < height:
                return True
        return False

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
        self.list_data = None
        self.num_lines = 0
        self.input_data = []
        self._parse_file()

    def _parse_file(self):
        with open(INPUT_FILEPATH, 'r') as f:
            raw_data = f.readlines()
        self.raw_data = [x.strip() for x in raw_data]
        self.list_data = [list(x) for x in self.raw_data]
        for row in self.list_data:
            self.num_lines += 1


def main():
    data = InputData()
    floor_map = FloorMap(data.list_data, data.num_lines)
    floor_map.set_low_points()


main()
