INPUT_FILEPATH="day08_input.txt"
INPUT_FILEPATH="test_input.txt"
class UniqueDigit:
    # 1, 4, 7, 8
    def __init__(self, number):
        self.wires = None
        self.number = number
        if number == 1:
            self.unique_wires = 2
        elif number == 4:
            self.unique_wires = 4
        elif number == 7:
            self.unique_wires = 3
        elif number == 8:
            self.unique_wires = 7
        raise ValueError(f'{number} is not a unique digit')

    def __str__(self):
        return f'[{self.number}]: {self.wires}'

    def set_wires(self, wires):
        """Set wires for digit, e.g. 1=>ab"""

        if len(wires) != self.unique_wires:
            raise ValueError(f'{wires} is the incorrect length of {self.unique_wires}')
        self.wires = wires


class DebugDisplay:
    def __init__(self, data):
        self.data = data


class InputData:
    def __init__(self):
        self.raw_data = None
        self.input_data = {}
        self._parse_file()

    def _parse_file(self):
        with open(INPUT_FILEPATH, 'r') as f:
            raw_data = f.readlines()
        self.raw_data = [x.strip() for x in raw_data]
        for line in self.raw_data:
            split_data = line.split('|')
            wire_data = split_data[0].strip()
            number_display = split_data[1].strip()
            self.input_data[wire_data] = number_display


def main():
    data = InputData()
    print(f'[!!] {data.input_data}')


main()
