INPUT_FILEPATH = "day07_input.txt"


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
        N = abs(num_steps)  # Use the sum of consecutive numbers formula
        fuel_consumed = int(N * ((1+N)/2))
        self.fuel += fuel_consumed

    def move_to(self, position):
        """Move to expected position and determine fuel"""

        num_steps = position - self.position
        self.step(num_steps)


class SimulateAlignment:
    def __init__(self, data):
        self.array_length = max(data) + 1
        self.crabs = [Crab(x) for x in data]
        self.total_fuel = 0

    def move_all_to(self, position):
        """Move all crabs to position"""

        for crab in self.crabs:
            crab.move_to(position)
            self.total_fuel += crab.fuel

    def reset_crabs(self):
        [crab.reset() for crab in self.crabs]
        self.total_fuel = 0

    def _find_min(self, arr):
        """Find minimum value in array and return index"""

        min_values = 0, arr[0]
        for index, value in enumerate(arr):
            min_value = min_values[1]
            if value < min_value:
                min_values = index, value
        return min_values

    def get_least_consumption(self):
        """Align crabs to position and determine which will have the least consumption

        :returns: Tuple (fuel, position)
        """

        fuel_consumption = [-1 for x in range(self.array_length)]
        for x in range(self.array_length):
            position = x
            self.move_all_to(position)
            fuel_consumption[position] = self.total_fuel
            self.reset_crabs()
        return self._find_min(fuel_consumption)


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
    position, min_fuel = simulate.get_least_consumption()
    print(f'[!!] Least fuel consumption: Position ({position}) with {min_fuel} fuel')


main()
