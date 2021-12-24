INPUT_FILEPATH="day04_input.txt"
INPUT_FILEPATH="test_input.txt"

class Board:
    def __init__(self, row_data):
        self.row1 = [(x, False) for x in row_data[0]]
        self.row2 = [(x, False) for x in row_data[1]]
        self.row3 = [(x, False) for x in row_data[2]]
        self.row4 = [(x, False) for x in row_data[3]]
        self.row5 = [(x, False) for x in row_data[4]]
        self.col1 = self._set_columns(0)
        self.col2 = self._set_columns(1)
        self.col3 = self._set_columns(2)
        self.col4 = self._set_columns(3)
        self.col5 = self._set_columns(4)
        self.bingo = False

    def _set_columns(self, index):
        column = [(self.row1[index], False),
                  (self.row2[index], False),
                  (self.row3[index], False),
                  (self.row4[index], False),
                  (self.row5[index], False)]
        return column

    def __str__(self):
        return (f'{self.row1}\n'
                f'{self.row2}\n'
                f'{self.row3}\n'
                f'{self.row4}\n'
                f'{self.row5}')

    def _check_row_or_column(self, rc_array):
        for (num, flag) in rc_array:
            if not flag:
                return False
        return True

    def check_bingo(self):
        if self._check_row_or_column(self.row1):
            self.bingo = True
        if self._check_row_or_column(self.row2):
            self.bingo = True
        if self._check_row_or_column(self.row3):
            self.bingo = True
        if self._check_row_or_column(self.row4):
            self.bingo = True
        if self._check_row_or_column(self.row5):
            self.bingo = True
        if self._check_col_or_column(self.col1):
            self.bingo = True
        if self._check_col_or_column(self.col2):
            self.bingo = True
        if self._check_col_or_column(self.col3):
            self.bingo = True
        if self._check_col_or_column(self.col4):
            self.bingo = True
        if self._check_col_or_column(self.col5):
            self.bingo = True

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


def main():
    bingo = Bingo()
    # print(bingo.board1)


main()
