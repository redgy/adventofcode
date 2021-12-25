INPUT_FILEPATH="day07_input.txt"
INPUT_FILEPATH="test_input.txt"
class Crab:
    def __init__(self, position):
        self.starting_position = position
        self.position = position
        self.fuel = 0

    def __str__(self):
        return f'[{self.position}]: {self.fuel}'

    def reset(self):
        """Reset position and fuel"""

        self.position = self.starting_position
        self.fuel = 0

    def step(self, num_steps):
        """Step in a direction (negative number will go left)"""

        self.position += num_steps
        self.fuel += abs(num_steps)

    def move_to(self, position):
        """Move to expected position and determine fuel"""

        num_steps = position - self.position
        self.step(num_steps)


class SimulateAlignment:
    def __init__(self, data):
        self.crabs = [Crab(x) for x in data]


class InputData:
    def __init__(self):
        self.clean_data = None
        self._parse_file()

    def _parse_file(self):
        with open(INPUT_FILEPATH, 'r') as f:
            raw_data = f.readlines()
        self.clean_data = [int(x) for x in raw_data[0].split(',')]


def main():
    data = InputData()
    simulate = SimulateAlignment(data.clean_data)
    for crab in simulate.crabs:
        print(crab)


main()
