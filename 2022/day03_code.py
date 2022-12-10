from utils import get_input
from utils import print_results

FILENAME = 'day03_input_sample.txt'
# FILENAME = 'day03_input.txt'


def calculate_priority(item):
    """Calculate priority based off of shared item
        A = 65  Z = 90  --> subtract 38 to get 27-52
        a = 97  Z = 122  --> subtract 96 to get 1-26
    """

    if item.islower():
        return ord(item) - 96
    return ord(item) - 38


class Rucksack:
    def __init__(self, number, entry):
        self.number = number
        self.contents = entry
        half_index = int(len(entry)/2)
        self.compartment_one = entry[:half_index]
        self.compartment_two = entry[-half_index:]
        self.shared_item = None
        self.priority = 0

    def __str__(self):
        """To string method"""

        return (
            f"Rucksack #{self.number}\n"
            f"   Compartment #1: {self.compartment_one}\n"
            f"   Compartment #2: {self.compartment_two}"
        )

    def __repr__(self):
        return (
            f"Rucksack #{self.number}\n"
            f"   Compartment #1: {self.compartment_one}\n"
            f"   Compartment #2: {self.compartment_two}"
        )

    def find_shared_item(self):
        """Find the shared item in the compartments"""

        if self.shared_item is None:
            for item in self.compartment_one:
                if item in self.compartment_two:
                    self.shared_item = item

    def calculate_priority(self):
        """Calculate priority based off of shared item
            A = 65  Z = 90  --> subtract 38 to get 27-52
            a = 97  Z = 122  --> subtract 96 to get 1-26
        """

        if self.shared_item is None:
            self.find_shared_item()
        if self.shared_item.islower():
            self.priority = ord(self.shared_item) - 96
        else:
            self.priority = ord(self.shared_item) - 38


def get_data():
    """Get data from input"""

    return get_input(FILENAME, 'basic')


def initialize_rucksacks(data):
    return [Rucksack(index, x) for index, x in enumerate(data)]


def initialize_group_rucksacks(data):
    """Initialize rucksacks for part two"""

    group_rucksacks = []
    for index in range(0, len(data), 3):
        rucksack1 = Rucksack(index+1, data[index])
        rucksack2 = Rucksack(index+2, data[index+1])
        rucksack3 = Rucksack(index+3, data[index+2])
        group_rucksacks.append(GroupRucksack(rucksack1, rucksack2, rucksack3))
    return group_rucksacks


def get_total_priority(rucksacks):
    """Get total priority from all rucksacks

    :param list<Rucksack> rucksacks: List of all rucksacks
    :returns: Int. Total priority
    """

    total = 0
    for r in rucksacks:
        r.calculate_priority()
        total += r.priority
    return total


def main():
    data = get_data()
    rucksacks = initialize_rucksacks(data)
    total_priority = get_total_priority(rucksacks)
    print_results(total_priority, 'PART ONE: Total Priority')


if __name__ == '__main__':
    main()
