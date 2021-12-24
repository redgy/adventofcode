INPUT_FILEPATH="day04_input.txt"
INPUT_FILEPATH="test_input.txt"
# Answer is around 11k
class MarkedBoard:
    def __init__(self):
        for x in range(5):
            self.grid = [[False for x in range(5)]]

    def is_row_complete(self, row):
        number_of_marked_cells = 0
        for column in range(5):
            if self.grid[row][column]:
                number_of_marked_cells +=1
        return number_of_marked_cells == 5

    def is_column_complete(self, column):
        number_of_marked_cells = 0
        for row in range(5):
            if self.grid[row][column]:
                number_of_marked_cells +=1
        return number_of_marked_cells == 5

class NumberBoard:
    def __init__(self, row_data):
        self.marked_board = MarkedBoard()
        self.grid = [
            [x for x in row_data[0]],
            [x for x in row_data[1]],
            [x for x in row_data[2]],
            [x for x in row_data[3]],
            [x for x in row_data[4]]
        ]
        self.grid_transposed = [list(i) for i in zip(*self.grid)]
        self.bingo = False

    def __str__(self):
        to_string = ''
        for row in self.grid:
            for col in row:
                to_string += f'{col} '
            to_string += '\n'
        return to_string

    def check_array(self, matrix):
        for row in matrix:
            num_marked = 0
            for (num, flag) in row:
                if flag:
                    num_marked += 1
            if num_marked == 5:
                self.bingo = True

    def check_bingo(self):
        self.check_array(self.grid)
        if not self.bingo:
            self.check_array(self.grid_transposed)

    def mark_number(self, number):
        for row, data in enumerate(self.grid):
            for col, (num, flag) in enumerate(data):
                if num == number:
                    self.grid[row][col] = (num, True)
                    break
        self.check_bingo()

    def calculate_total(self):
        total = 0
        for row in self.grid:
            for (num, flag) in row:
                if not flag:
                    total += num
        return total

class InputData:
    def __init__(self):
        self.raw_data = None
        self._parse_file()
        self.numbers_data = self.raw_data[0]
        self.boards_data = self._parse_board_data(self.raw_data[1:])

    def _parse_file(self):
        with open(INPUT_FILEPATH, 'r') as f:
            raw_data = f.readlines()
            raw_data = [x.strip() for x in raw_data]
            raw_data = [x for x in raw_data if x]
        self.raw_data = raw_data

    def _parse_board_data(self, raw_data):
        data = []
        boards = []
        for row in raw_data:
            entry = [int(x) for x in row.split(' ') if x]
            data.append(entry)
            if len(data) == 5:
                boards.append(data)
                data = []
        return boards

def main():
    data = InputData()
    print(f'>> {data.boards_data}')
    # bingo = Bingo()
    # board, product = bingo.call_numbers()
    # print(f'[!!] Board #{board} BINGO')
    # print(f'[!!] Product of winning board: {product}')

main()
