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
    def __init__(self, number, signal_pattern=''):
        if number == 1:
            self.num_unique_signal_pattern = MAP_WIRES[1]
        elif number == 4:
            self.num_unique_signal_pattern = MAP_WIRES[4]
        elif number == 7:
            self.num_unique_signal_pattern = MAP_WIRES[7]
        elif number == 8:
            self.num_unique_signal_pattern = MAP_WIRES[8]
        else:
            raise ValueError(f'{number} is not a unique digit')
        self.number = number
        self.signal_pattern = self.set_signal_pattern(signal_pattern) if signal_pattern else ''

    def __str__(self):
        return f'[{self.number}]: {self.signal_pattern}'

    def set_signal_pattern(self, signal_pattern):
        """Set signal_pattern for digit, e.g. 1=>ab"""

        if len(signal_pattern) != self.num_unique_signal_pattern:
            raise ValueError(f'{signal_pattern} is the incorrect length of {self.num_unique_signal_pattern}')
        return signal_pattern


class DebugDisplay:
    def __init__(self, data):
        self.data = data
        self.one = None
        self.four = None
        self.seven = None
        self.eight = None

    def _is_unique_digits_initialized(self):
        return self.one and self.four and self.seven and self.eight

    def get_unique_digit_occurrences(self):
        count = 0
        unique_pattern_array = MAP_WIRES.values()
        for line in self.data:
            digit_array = line[1]
            for digit in digit_array:
                if len(digit) in unique_pattern_array:
                    count += 1
        return count

    def get_signal_patterns(self):
        for line in self.data:
            if self._is_unique_patterns_initialized():
                break
            signal_patterns = line[0]
            self.set_unique_pattern(signal_patterns)
            print(signal_patterns)

    def set_unique_pattern(self, signal_patterns):
        for signal_pattern in signal_patterns:
            if len(signal_pattern) == MAP_WIRES[1]:
                self.one = UniqueDigit(1, signal_pattern)
            elif len(signal_pattern) == MAP_WIRES[4]:
                self.four = UniqueDigit(4, signal_pattern)
            elif len(signal_pattern) == MAP_WIRES[7]:
                self.seven = UniqueDigit(7, signal_pattern)
            elif len(signal_pattern) == MAP_WIRES[8]:
                self.eight = UniqueDigit(8, signal_pattern)

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
            signal_patterns = split_data[0].strip()
            signal_patterns = signal_patterns.split(' ')
            digit_output = split_data[1].strip()
            digit_output = digit_output.split(' ')
            to_add = (signal_patterns, digit_output)
            self.input_data.append(to_add)


def main():
    data = InputData()
    debug = DebugDisplay(data.input_data)
    count = debug.get_unique_digit_occurrences()
    print(f'[!!] Unique digit count: {count}')


main()
