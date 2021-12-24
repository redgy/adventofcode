INPUT_FILEPATH="day04_input.txt"
INPUT_FILEPATH="test_input.txt"

class Board:
    def __init__(self, row_data):
        self.grid = [[(x, False) for x in row_data[0]],
            [(x, False) for x in row_data[1]],
            [(x, False) for x in row_data[2]],
            [(x, False) for x in row_data[3]],
            [(x, False) for x in row_data[4]]
        ]
        self.bingo = False

    def __str__(self):
        to_string = ''
        for row in self.grid:
            for col in row:
                to_string += f'{col} '
            to_string += '\n'
        return to_string

    def check_bingo(self):
        for row in self.grid:
            num_marked = 0
            for (num, flag) in row:
                if flag:
                    num_marked += 1
            if num_marked == 5:
                self.bingo = True

    def mark_number(self, number):
        print(f'[!!] Calling {number}')
        for row in self.grid:
            for (num, flag) in row:
                print(f'  |-> {num}')
                if num == number:
                    flag = True

class Bingo:
    def __init__(self):
        self.bingo_numbers = []
        self.board1 = None
        self.board2 = None
        self.board3 = None
        self.init_boards()

    def init_boards(self):
        raw_data = self._parse_file()
        self.bingo_numbers = raw_data[0]
        self.board1 = Board(self._clean_row_data(raw_data[1:6]))
        self.board2 = Board(self._clean_row_data(raw_data[6:11]))
        self.board3 = Board(self._clean_row_data(raw_data[11:16]))

    def _clean_row_data(self, raw_data):
        clean_data = []
        for row in raw_data:
            split_data = row.split(' ')
            clean_data.append([int(x) for x in split_data if x])
        return clean_data

    def _parse_file(self):
        with open(INPUT_FILEPATH, 'r') as f:
            raw_data = f.readlines()
            raw_data = [x.strip() for x in raw_data]
            raw_data = [x for x in raw_data if x]
        return raw_data

    def call_numbers(self):
        for num in self.bingo_numbers:
            self.board1.mark_number(num)
            self.board2.mark_number(num)
            self.board3.mark_number(num)


def main():
    bingo = Bingo()
    bingo.call_numbers()
    print(bingo.board1)


main()
