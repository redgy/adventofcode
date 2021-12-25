INPUT_FILEPATH="day06_input.txt"
INPUT_FILEPATH="test_input.txt"
NUMBER_OF_DAYS=5
class Lantern:
    def __init__(self, timer=6, is_new=False):
        self.is_new = is_new
        if is_new:
            timer = 8
        self.timer = timer

    def __str__(self):
        to_string = '[NEW] ' if self.is_new else '[OLD] '
        to_string += f'{self.timer}'
        return to_string

    def decrement(self):
        """Decrement timer with some logic depending on if lantern is new"""

        if self.is_new:
            self.is_new = False  # So next time it will decrement
        else:
            self.timer -= 1
            if self.timer < 0:
                self.timer = 6


class SimulaterLanterns:
    def __init__(self, data):
        self.data = data
        self.lanterns = [Lantern(timer=x) for x in data]

    def _print_lanterns(self, day=None):
        """Helper method to print lanterns"""

        to_string = f'After {day:>2} day(s): ' if day else 'Initial state: '
        for lantern in self.lanterns:
            to_string += f'{lantern.timer},'
        print(f'{to_string[:-1]}')

    def simulate_days(self, number_of_days):
        """Simulates life of lanterns after a number of days"""

        for x in range(number_of_days):
            self._print_lanterns(x)
            for lantern in self.lanterns:
                lantern.decrement()
                if lantern.timer == 0:
                    self.lanterns.append(Lantern(is_new=True))

    def reset_simulation(self):
        """Reset simulation back to initial state"""

        self.lanterns = [Lantern(timer=x) for x in data]

    def get_total_lanterns(self):
        """Returns total number of lanterns in simulation"""

        return len(self.lanterns)


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
    simulator = SimulaterLanterns(data.clean_data)
    simulator.simulate_days(NUMBER_OF_DAYS)
    number_of_lanterns = simulator.get_total_lanterns()
    print(f'[!!] After {NUMBER_OF_DAYS} days, total number of lanterns: {number_of_lanterns}')


main()
