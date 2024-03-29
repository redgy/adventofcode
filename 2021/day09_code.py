INPUT_FILEPATH = "day09_input.txt"


class Cell:
    def __init__(self, height, x, y, max_x, max_y):
        self.height = int(height)
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
            to_string += f' ({self.risk_level})'
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
        is_x_valid = (x >= 0 and x < self.max_x)
        is_y_valid = (y >= 0 and y < self.max_y)
        return is_x_valid and is_y_valid


class Basin:
    def __init__(self, low_point_cell, location_list):
        self.low_point_cell = low_point_cell
        self.location_list = list(set(location_list))
        self.size = len(self.location_list)

    def __str__(self):
        to_str = f'{self.low_point_cell}--{self.size}--> '
        for location in self.location_list:
            to_str += f'({location.x}, {location.y}) '
        return to_str


class FloorMap:
    def __init__(self, list_data, num_lines):
        single_row = list_data[0]
        self.num_cols = len(single_row)
        self.num_rows = num_lines
        self.floor_map = [[None for x in range(self.num_cols)] for x in range(self.num_rows)]
        self.low_point_cells = []
        self.basins = []
        self._populate_floor_map(list_data)
        self._set_low_points()
        self._find_basins()

    def _populate_floor_map(self, data):
        for row, row_list in enumerate(data):
            for col, value in enumerate(row_list):
                new_cell = Cell(value, row, col, self.num_rows, self.num_cols)
                self.floor_map[row][col] = new_cell

    def _set_low_points(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                current_cell = self.floor_map[row][col]
                self._set_cells_low_point(current_cell)

    def _set_cells_low_point(self, cell):
        coords_list = cell.get_adjacent_cells_coords_list()
        is_min = True
        for single_coords in coords_list:
            if self._is_other_cell_lower(cell.height, single_coords):
                is_min = False
        if is_min:
            cell.is_low_point = True
            cell.risk_level = cell.height+1
            self.low_point_cells.append(cell)

    def _is_other_cell_lower(self, height, cell_tuple):
        if cell_tuple:
            row = cell_tuple[0]
            col = cell_tuple[1]
            other_height = self.floor_map[row][col].height
            if other_height <= height:
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

    def _find_basins(self):
        for low_point_cell in self.low_point_cells:
            location_list = self._find_basin_recursively(low_point_cell, [low_point_cell])
            new_basin = Basin(low_point_cell, location_list)
            self.basins.append(new_basin)

    def _find_basin_recursively(self, current_cell, location_list):
        coords_list = current_cell.get_adjacent_cells_coords_list()
        for single_coord in coords_list:
            row = single_coord[0]
            col = single_coord[1]
            adjacent_cell = self.floor_map[row][col]
            is_one_bigger = (adjacent_cell.height == current_cell.height+1)
            is_not_nine = adjacent_cell.height != 9
            if is_one_bigger and is_not_nine:
                location_list.append(adjacent_cell)
                self._find_basin_recursively(adjacent_cell, location_list)
        return location_list

    def get_sum_of_risk_levels(self):
        total = 0
        for cell in self.low_point_cells:
            total += cell.risk_level
        return total

    def get_product_of_top_three_basins(self):
        size_array = [x.size for x in self.basins]
        product = 1
        for x in range(3):
            top = max(size_array)
            product *= top
            size_array.remove(max(size_array))
        return product


class Simple:
    def __init__(self, list_data, num_lines):
        single_row = list_data[0]
        self.num_cols = len(single_row)
        self.num_rows = num_lines
        self.basin_size_list = []
        self.risk_sum = 0
        self.floor_map = [[None for x in range(self.num_cols)] for x in range(self.num_rows)]
        self._populate_map(list_data)
        self.calculate_low_points()

    def _populate_map(self, data):
        for row, row_list in enumerate(data):
            for col, value in enumerate(row_list):
                self.floor_map[row][col] = int(value)

    def calculate_low_points(self):
        risk_sum = 0
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                height = self.floor_map[row][col]
                is_low_point = self._is_low_point(height, row, col)
                if is_low_point:
                    risk_sum += height+1
                    basin_size = self._get_basin_size(height, row, col)
                    self.basin_size_list.append(basin_size)
        self.risk_sum = risk_sum

    def calculate_basin_product(self):
        all_basins = self.basin_size_list
        product = 1
        for x in range(3):
            top_size = max(all_basins)
            product *= top_size
            all_basins.remove(top_size)
        return product

    def _is_low_point(self, height, row, col):
        adjacent_row = row

        # Check left
        adjacent_col = col-1
        if self._is_valid_col_range(adjacent_col):
            adjacent_height = self.floor_map[adjacent_row][adjacent_col]
            if adjacent_height <= height:
                return False

        # Check right
        adjacent_col = col+1
        if self._is_valid_col_range(adjacent_col):
            adjacent_height = self.floor_map[adjacent_row][adjacent_col]
            if adjacent_height <= height:
                return False

        adjacent_col = col

        # Check up
        adjacent_row = row-1
        if self._is_valid_row_range(adjacent_row):
            adjacent_height = self.floor_map[adjacent_row][adjacent_col]
            if adjacent_height <= height:
                return False

        # Check down
        adjacent_row = row+1
        if self._is_valid_row_range(adjacent_row):
            adjacent_height = self.floor_map[adjacent_row][adjacent_col]
            if adjacent_height <= height:
                return False

        return True

    def _is_valid_col_range(self, index):
        return index >= 0 and index < self.num_cols

    def _is_valid_row_range(self, index):
        return index >= 0 and index < self.num_rows

    def _is_part_of_basin(self, height, adjacent_height):
        return height < adjacent_height and adjacent_height != 9

    def _get_basin_size(self, height, row, col):
        initial_locations = set([(row, col)])
        basin_locations = self._get_basin_locations(initial_locations, height, row, col)
        return len(basin_locations)

    def _get_basin_locations(self, basin_locations, height, row, col):
        adjacent_row = row

        # Check left
        adjacent_col = col-1
        if self._is_valid_col_range(adjacent_col):
            adjacent_height = self.floor_map[adjacent_row][adjacent_col]
            if self._is_part_of_basin(height, adjacent_height):
                basin_locations.add((adjacent_row, adjacent_col))
                self._get_basin_locations(basin_locations, adjacent_height, adjacent_row, adjacent_col)

        # Check right
        adjacent_col = col+1
        if self._is_valid_col_range(adjacent_col):
            adjacent_height = self.floor_map[adjacent_row][adjacent_col]
            if self._is_part_of_basin(height, adjacent_height):
                basin_locations.add((adjacent_row, adjacent_col))
                self._get_basin_locations(basin_locations, adjacent_height, adjacent_row, adjacent_col)

        adjacent_col = col

        # Check up
        adjacent_row = row-1
        if self._is_valid_row_range(adjacent_row):
            adjacent_height = self.floor_map[adjacent_row][adjacent_col]
            if self._is_part_of_basin(height, adjacent_height):
                basin_locations.add((adjacent_row, adjacent_col))
                self._get_basin_locations(basin_locations, adjacent_height, adjacent_row, adjacent_col)

        # Check down
        adjacent_row = row+1
        if self._is_valid_row_range(adjacent_row):
            adjacent_height = self.floor_map[adjacent_row][adjacent_col]
            if self._is_part_of_basin(height, adjacent_height):
                basin_locations.add((adjacent_row, adjacent_col))
                self._get_basin_locations(basin_locations, adjacent_height, adjacent_row, adjacent_col)

        return basin_locations


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
    simple_floor_map = Simple(data.list_data, data.num_lines)
    floor_map = FloorMap(data.list_data, data.num_lines)
    print('[!!] Sum of risk levels: \n'
          f'    |--simple-floor-map--> {simple_floor_map.risk_sum}\n'
          f'    |--object-floor-map--> {floor_map.get_sum_of_risk_levels()}')  # End part I
    print('[!!] Product of basin sizes: \n'
          f'    |--simple-floor-map--> {simple_floor_map.calculate_basin_product()}\n'
          f'    |--object-floor-map--> {floor_map.get_product_of_top_three_basins()}')  # End part II
    # ^^^ I never figured out the flaw in my logic for object-floor-map


main()
