INPUT_FILEPATH="day08_input.txt"
INPUT_FILEPATH="test_input.txt"
MAP_WIRES= {
    1: 2,
    4: 4,
    7: 3,
    8: 7
}
class UniqueDigit:
    # 1, 4, 7, 8
    def __init__(self, number, wires=''):
        if number == 1:
            self.unique_wires = MAP_WIRES[1]
        elif number == 4:
            self.unique_wires = MAP_WIRES[4]
        elif number == 7:
            self.unique_wires = MAP_WIRES[7]
        elif number == 8:
            self.unique_wires = MAP_WIRES[8]
        else:
            raise ValueError(f'{number} is not a unique digit')
        self.number = number
        self.wires = self.set_wires(wires) if wires else ''
        print(self)

    def __str__(self):
        return f'[{self.number}]: {self.wires}'

    def set_wires(self, wires):
        """Set wires for digit, e.g. 1=>ab"""

        if len(wires) != self.unique_wires:
            raise ValueError(f'{wires} is the incorrect length of {self.unique_wires}')
        return wires


class DebugDisplay:
    def __init__(self, data):
        self.data = data
        self.one = None
        self.four = None
        self.seven = None
        self.eight = None

    def _is_unique_digits_initialized(self):
        return self.one and self.four and self.seven and self.eight

    def get_wires(self):
        for line in self.data:
            if self._is_unique_digits_initialized():
                break
            wire_array = line[0]
            self.set_unique_digit(wire_array)
            print(wire_array)

    def set_unique_digit(self, wire_array):
        for wire in wire_array:
            if len(wire) == MAP_WIRES[1]:
                self.one = UniqueDigit(1, wire)
            elif len(wire) == MAP_WIRES[4]:
                self.four = UniqueDigit(4, wire)
            elif len(wire) == MAP_WIRES[7]:
                self.seven = UniqueDigit(7, wire)
            elif len(wire) == MAP_WIRES[8]:
                self.eight = UniqueDigit(8, wire)

class InputData:
    def __init__(self):
        self.raw_data = None
        self.input_data = []
        self._parse_file()

    def _parse_file(self):
        with open(INPUT_FILEPATH, 'r') as f:
            raw_data = f.readlines()
        self.raw_data = [x.strip() for x in raw_data]
        for line in self.raw_data:
            split_data = line.split('|')
            wire_data = split_data[0].strip()
            number_display = split_data[1].strip()
            wire_data = wire_data.split(' ')
            to_add = (wire_data, number_display)
            self.input_data.append(to_add)


def main():
    data = InputData()
    debug = DebugDisplay(data.input_data)
    debug.get_wires()


main()
