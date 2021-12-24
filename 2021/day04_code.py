INPUT_FILEPATH="day04_input.txt"
INPUT_FILEPATH="test_input.txt"
# Answer is around 11k
class MarkedCard:
    def __init__(self):
        for x in range(5):
            self.grid = [[False for x in range(5)] for x in range(5)]

    def __str__(self):
        to_string = '------------------\n'
        for row in self.grid:
            to_string += '|'
            for column in row:
                mark_string = 'X' if column else 'O'
                to_string += f'{mark_string:>3}'
            to_string += ' |\n'
        to_string += '------------------'
        return to_string

    def mark_cell(self, row, column):
        self.grid[row][column] = True

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

    def has_bingo(self):
        for x in range(5):
            if self.is_row_complete(x):
                return True
            if self.is_column_complete(x):
                return True
        return False


class BingoCard:
    def __init__(self, row_data):
        self.marked_card = MarkedCard()
        self.grid = [
            [x for x in row_data[0]],
            [x for x in row_data[1]],
            [x for x in row_data[2]],
            [x for x in row_data[3]],
            [x for x in row_data[4]]
        ]
        self.bingo = False

    def __str__(self):
        to_string = '------------------\n'
        for row in self.grid:
            to_string += '|'
            for column in row:
                to_string += f'{column:>3}'
            to_string += ' |\n'
        to_string += '------------------'
        return to_string

    def mark_number(self, number):
        for row, row_data in enumerate(self.grid):
            for column, column_data in enumerate(row_data):
                value = self.grid[row][column]
                if value == number:
                    self.marked_card.mark_cell(row, column)
                    if self.marked_card.has_bingo():
                        self.bingo = True


class SimulateBingo:
    def __init__(self, bingo_numbers, cards_data):
        self.bingo_numbers = bingo_numbers
        self.cards = []
        for card in cards_data:
            self.cards.append(BingoCard(card))

    def call_numbers(self):
        for number in self.bingo_numbers:
            for card in self.cards:
                card.mark_number(number)
                if card.bingo:
                    break


class InputData:
    def __init__(self):
        self.raw_data = None
        self._parse_file()
        self.numbers_data = self._parse_number_data(self.raw_data[0])
        self.cards_data = self._parse_card_data(self.raw_data[1:])

    def _parse_file(self):
        with open(INPUT_FILEPATH, 'r') as f:
            raw_data = f.readlines()
            raw_data = [x.strip() for x in raw_data]
            raw_data = [x for x in raw_data if x]
        self.raw_data = raw_data

    def _parse_number_data(self, raw_data):
        return [int(x) for x in raw_data.split(',')]

    def _parse_card_data(self, raw_data):
        data = []
        cards = []
        for row in raw_data:
            entry = [int(x) for x in row.split(' ') if x]
            data.append(entry)
            if len(data) == 5:
                cards.append(data)
                data = []
        return cards


def main():
    data = InputData()
    simulate = SimulateBingo(data.numbers_data, data.cards_data)
    simulate.call_numbers()
    for card in simulate.cards:
        print(f'{card.marked_card}')
    # bingo = Bingo()
    # card, product = bingo.call_numbers()
    # print(f'[!!] Card #{card} BINGO')
    # print(f'[!!] Product of winning card: {product}')

main()
