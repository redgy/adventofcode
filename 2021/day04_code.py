INPUT_FILEPATH="day04_input.txt"
# INPUT_FILEPATH="test_input.txt"
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
        self.grid = [[(x, False) for x in row_data[0]],
            [(x, False) for x in row_data[1]],
            [(x, False) for x in row_data[2]],
            [(x, False) for x in row_data[3]],
            [(x, False) for x in row_data[4]]
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
        # if number == 24:
        #     print(f'[!!] {self}')
        self.check_bingo()

    def calculate_total(self):
        total = 0
        for row in self.grid:
            for (num, flag) in row:
                if not flag:
                    total += num
        return total

class Bingo:
    def __init__(self):
        self.bingo_numbers = []
        self.boards = []
        self.init_boards()

    def init_boards(self):
        raw_data = self._parse_file()
        self.bingo_numbers = [int(x) for x in raw_data[0].split(',')]
        number_of_boards = int((len(raw_data))/5)
        start = 1
        for x in range(number_of_boards):
            end = start+5
            clean_data = self._clean_row_data(raw_data[start:end])
            self.boards.append(Board(clean_data))
            start = end

    def _clean_row_data(self, raw_data):
        clean_data = []
        for row in raw_data:
            split_data = row.split(' ')
            clean_data.append([int(x) for x in split_data if x])
        return clean_data

    def call_numbers(self):
        num_called = []
        for num in self.bingo_numbers:
            num_called.append(num)
            for index, board in enumerate(self.boards, start=1):
                board.mark_number(num)
                if board.bingo:
                    print(f'[!!] Numbers called: {num_called}')
                    return index, board.calculate_total() * num


class InputData:
    def __init__(self):
        self.raw_data = None
        self._parse_file()
        self.numbers_data = self.raw_data[0]
        self.boards_data = self.raw_data[1:]

    def _parse_file(self):
        with open(INPUT_FILEPATH, 'r') as f:
            raw_data = f.readlines()
            raw_data = [x.strip() for x in raw_data]
            raw_data = [x for x in raw_data if x]
        self.raw_data = raw_data

def main():
    data = InputData()
    print(f'[!!] {data.boards_data}')
    # bingo = Bingo()
    # board, product = bingo.call_numbers()
    # print(f'[!!] Board #{board} BINGO')
    # print(f'[!!] Product of winning board: {product}')

main()
