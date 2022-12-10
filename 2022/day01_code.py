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


def find_max_elf(elves):
    """Part one is finding the elf holding the most calories

    :param list<Elf> elves: List of Elf objects
    :returns: Elf. The elf holding the most calories
    """

    max_elf = elves[0]
    for elf in elves:
        if elf.calorie_sum > max_elf.calorie_sum:
            max_elf = elf
    return max_elf


def main():
    data = get_data()
    elves = initialize_elves(data)
    pp.pprint(elves)
    max_elf = find_max_elf(elves)  # PART ONE
    pp.pprint(max_elf)


if __name__ == '__main__':
    main()
