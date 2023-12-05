INPUT_FILEPATH = "day04_input.txt"


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
                number_of_marked_cells += 1
        return number_of_marked_cells == 5

    def is_column_complete(self, column):
        number_of_marked_cells = 0
        for row in range(5):
            if self.grid[row][column]:
                number_of_marked_cells += 1
        return number_of_marked_cells == 5

    def has_bingo(self):
        for x in range(5):
            if self.is_row_complete(x):
                return True
            if self.is_column_complete(x):
                return True
        return False


class BingoCard:
    def __init__(self, card_number, row_data):
        self.card_number = card_number
        self.marked_card = MarkedCard()
        self.grid = [
            [x for x in row_data[0]],
            [x for x in row_data[1]],
            [x for x in row_data[2]],
            [x for x in row_data[3]],
            [x for x in row_data[4]]
        ]
        self.bingo = False
        self.bingo_numbers = []
        self.winning_product = -1
        self.winning_number = -1

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
        self.bingo_numbers.append(number)
        for row, row_data in enumerate(self.grid):
            for column, column_data in enumerate(row_data):
                value = self.grid[row][column]
                if value == number:
                    self.marked_card.mark_cell(row, column)
                    if self.marked_card.has_bingo():
                        self.bingo = True

    def calculate_product(self, winning_number):
        total_sum = 0
        for row, row_data in enumerate(self.grid):
            for column, column_data in enumerate(row_data):
                if not self.marked_card.grid[row][column]:
                    value = self.grid[row][column]
                    total_sum += value
        self.winning_number = winning_number
        self.winning_product = total_sum * winning_number


class SimulateBingo:
    def __init__(self, bingo_numbers, cards_data):
        self.bingo_numbers = bingo_numbers
        self.cards = []
        for card_number, card_data in enumerate(cards_data):
            self.cards.append(BingoCard(card_number, card_data))
        self.win_log = {x: {} for x in range(len(self.cards))}

    def call_numbers(self):
        recent_win = -1
        for bingo_number in self.bingo_numbers:
            for card in self.cards:
                if not card.bingo:
                    card.mark_number(bingo_number)
                if card.bingo:
                    self.record_win(bingo_number, card)
        return self.get_winner()

    def record_win(self, winning_number, card):
        if not self.win_log[card.card_number]:
            card.calculate_product(winning_number)
            self.win_log[card.card_number] = card
            self.win_log['last_winner'] = card.card_number

    def get_winner(self):
        winning_card_number = self.win_log['last_winner']
        return self.win_log[winning_card_number]


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
    winning_card = simulate.call_numbers()
    print(f'Called the following numbers: {winning_card.bingo_numbers}')
    print(winning_card)
    print(winning_card.marked_card)
    print(f'>>> BINGO ON {winning_card.winning_number}')
    print(f' -- Card Number: {winning_card.card_number}')
    print(f' -- Product: {winning_card.winning_product}')


main()
