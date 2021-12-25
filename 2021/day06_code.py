INPUT_FILEPATH="day06_input.txt"
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
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            self.is_new = False


class SimulateLanterns:
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
            # self._print_lanterns(x)
            number_of_new_lanterns = 0
            for lantern in self.lanterns:
                lantern.decrement()
                if lantern.timer == 6 and not lantern.is_new:
                    number_of_new_lanterns += 1
            for new_lantern in range(number_of_new_lanterns):
                self.lanterns.append(Lantern(is_new=True))
        # self._print_lanterns(number_of_days)

    def reset_simulation(self):
        """Reset simulation back to initial state"""

        self.lanterns = [Lantern(timer=x) for x in data]

    def get_total_lanterns(self):
        """Returns total number of lanterns in simulation"""

        return len(self.lanterns)


class SimpleSimulater:
    def __init__(self, data):



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
    part_one = SimulateLanterns(data.clean_data)
    part_one.simulate_days(80)
    number_of_lanterns = part_one.get_total_lanterns()
    print(f'[!!] Total Lanterns (I): {number_of_lanterns}')

    part_two = SimpleSimulater(data.clean_data)


main()
