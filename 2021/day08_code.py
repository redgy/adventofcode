INPUT_FILEPATH="day08_input.txt"
INPUT_FILEPATH="test_input.txt"
MAP_PATTERNS= {
    1: 2,
    4: 4,
    7: 3,
    8: 7
}
class DigitalNumber:
    def __init__(self, number, signal_pattern=''):
        self.number = number
        self.length_of_code = len(signal_pattern)
        self.signal_pattern = self.set_signal_pattern(signal_pattern) if signal_pattern else ''
        print(self)

    def __str__(self):
        return f'[{self.number}]: {self.signal_pattern}'

    def __contains__(self, other):
        """Does number contains pattern from other number"""
        for pattern_bit in other.signal_pattern:
            if not pattern_bit in self.signal_pattern:
                return False
        return True

    def set_signal_pattern(self, signal_pattern):
        """Set signal_pattern for digit, e.g. 1=>ab"""

        if len(signal_pattern) != self.num_unique_signal_pattern:
            raise ValueError(f'{signal_pattern} is the incorrect length of {self.num_unique_signal_pattern}')
        pattern_list = list(signal_pattern)
        pattern_list.sort()
        return pattern_list


class DebugDisplay:
    def __init__(self, data):
        self.data = data
        self.zero = None
        self.one = None
        self.two = None
        self.three = None
        self.four = None
        self.five = None
        self.six = None
        self.seven = None
        self.eight = None
        self.nine = None

    def reset_numbers(self):
        self.zero = None
        self.one = None
        self.two = None
        self.three = None
        self.four = None
        self.five = None
        self.six = None
        self.seven = None
        self.eight = None
        self.nine = None

    def get_unique_digit_occurrences(self):
        count = 0
        unique_pattern_array = MAP_PATTERNS.values()
        for line in self.data:
            digit_array = line[1]
            for digit in digit_array:
                if len(digit) in unique_pattern_array:
                    count += 1
        return count

    def get_digital_output(self):
        digital_outputs = []
        for line in self.data:
            signal_patterns = line[0]
            self.set_pattern(signal_patterns)
            print(signal_patterns)
            break

    def set_pattern(self, signal_patterns):
        for signal_pattern in signal_patterns:
            self._set_pattern(signal_pattern)
            self._set_pattern_for_length_of_five(signal_pattern)
            self._set_pattern_for_length_of_six(signal_pattern)

    def _set_pattern(self, signal_pattern):
        """Set unique pattern for 1, 4, 7, 8"""

        length_of_code = len(signal_pattern)
        if length_of_code == MAP_PATTERNS[1]:
            self.one = DigitalNumber(1, signal_pattern)
        elif length_of_code == MAP_PATTERNS[4]:
            self.four = DigitalNumber(4, signal_pattern)
        elif length_of_code == MAP_PATTERNS[7]:
            self.seven = DigitalNumber(7, signal_pattern)
        elif length_of_code == MAP_PATTERNS[8]:
            self.eight = DigitalNumber(8, signal_pattern)

    def _set_pattern_for_length_of_five(self, signal_pattern):
        """Set pattern for 2, 3, 5"""

        length_of_code = len(signal_pattern)
        if length_of_code == 5:
            print(signal_pattern)
            pass

    def _set_pattern_for_length_of_six(self, signal_pattern):
        """Set pattern for 0, 6, 9"""

        length_of_code = len(signal_pattern)
        if length_of_code == 6:
            pass

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
    debug.get_digital_output()
    print(f'[!!] Unique digit count: {count}')


main()
