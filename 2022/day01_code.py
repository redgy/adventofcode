from utils import get_input
from utils import pp

FILENAME = 'day01_input_sample.txt'
# FILENAME = 'day01_input.txt'


class Elf:
    def __init__(self, number, calorie_list_string):
        """Constructor

        :int number: Numbered elf from input
        :list<str> calorie_list_string: List of calories elf is holding
        """

        self._number = number
        self._calorie_list = [int(x) for x in calorie_list_string]
        self._calorie_sum = sum(self._calorie_list)

    def __str__(self):
        """To string method"""

        return (
            f"ELF #{self._number}\n"
            f"   Calorie list: {self._calorie_list}\n"
            f"   Calorie sum: {self._calorie_sum}"
        )

    def __repr__(self):
        return (
            f"ELF #{self._number}\n"
            f"   Calorie list: {self._calorie_list}\n"
            f"   Calorie sum: {self._calorie_sum}"
        )

    def __eq__(self, other):
        return self.number == other.number

    @property
    def number(self):
        return self._number

    @property
    def calorie_list(self):
        return self._calorie_list

    @property
    def calorie_sum(self):
        return self._calorie_sum


def get_data():
    """Get data from input"""

    return get_input(FILENAME, 'basic')


def initialize_elves(data):
    """Initialize the list of elves from input

    :param list data: List of data from input; includes an entry for empty lines
    :returns: List of Elf objects
    """

    elves = []
    calorie_list = []
    elf_number = 1
    for index, entry in enumerate(data):
        if entry  == '':
            elves.append(Elf(elf_number, calorie_list))
            calorie_list = []
            elf_number += 1
            continue
        calorie_list.append(entry)
    elves.append(Elf(elf_number, calorie_list))  # add last elf from list
    return elves


def get_calorie_total(elves, how_many):
    """Get total of max N(how many) elves from list

    :param list<Elf> elves: List of Elf objects
    :param int how_many: How many elves you want for max (e.g. top 1, top 3)
    :returns: Elf. The elf holding the most calories
    """

    max_elves = []
    while len(max_elves) < how_many:
        max_elf = elves[0]
        for elf in elves:
            if elf in max_elves:
                continue
            if elf.calorie_sum > max_elf.calorie_sum:
                max_elf = elf
        max_elves.append(max_elf)
    calorie_totals = [x.calorie_sum for x in max_elves]
    return sum(calorie_totals)


def print_results(blurb, results):
    print(blurb)
    print('-------')
    pp.pprint(results)
    print('')


def main():
    data = get_data()
    elves = initialize_elves(data)
    max_elf = get_calorie_total(elves, 1)  # PART ONE
    max_three_elves = get_calorie_total(elves, 3)  # PART TWO
    print_results('PART ONE', max_elf)
    print_results('PART TWO', max_three_elves)


if __name__ == '__main__':
    main()
