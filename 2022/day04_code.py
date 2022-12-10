from utils import get_input
from utils import print_results

FILENAME = 'day04_input_sample.txt'
FILENAME = 'day04_input.txt'


class Section:
    def __init__(self, entry):
        self.low, self.high = entry.split('-')

    def fully_contains(self, other):
        """Returns boolean depending if self fully contains other"""

        return other.low >= self.low and other.high <= self.high

    def __str__(self):
        """To string method"""

        return f"({self.low}, {self.high})"

    def __repr__(self):
        return f"({self.low}, {self.high})"


class ElfPair:
    def __init__(self, entry):
        one, two = entry.split(',')
        self.one = Section(one)
        self.two = Section(two)

    def __str__(self):
        """To string method"""

        return (
            f"One: {self.one}\n"
            f"Two: {self.two}"
        )

    def __repr__(self):
        return (
            f"One: {self.one}\n"
            f"Two: {self.two}"
        )

    def fully_contains(self):
        """Returns boolean if either sections fully contains the other"""

        return self.one.fully_contains(self.two) or self.two.fully_contains(self.one)


def get_data():
    """Get data from input"""

    return get_input(FILENAME, 'basic')


def initialize_pairs(data):
    """Initialize pair of assignments"""

    elf_pairs = []
    for entry in data:
        elf_pairs.append(ElfPair(entry))
    return elf_pairs


def get_fully_contains_count(elf_pairs):
    """Gets count of elf pairs that have assignments that fully contain the other"""

    count = 0
    for pair in elf_pairs:
        if pair.fully_contains():
            count += 1
    return count


def main():
    data = get_data()
    elf_pairs = initialize_pairs(data)
    fully_contains_count = get_fully_contains_count(elf_pairs)
    print_results(fully_contains_count, 'PART ONE: Number of fully contained assignments')


if __name__ == '__main__':
    main()
