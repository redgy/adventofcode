INPUT_FILEPATH="day08_input.txt"
INPUT_FILEPATH="test_input.txt"
MAP_PATTERNS= {
    1: 2,
    4: 4,
    7: 3,
    8: 7
}
class SignalPattern:
    def __init__(self, signal_pattern_str):
        pattern_as_list = list(signal_pattern_str)
        pattern_as_list.sort()
        self.code = pattern_as_list
        self.str = ''.join(self.code)
        self.length = len(self.code)

    def __str__(self):
        return self.str

    def __eq__(self, other):
        return self.code == other.code

    def contains(self, other):
        for pattern_bit in other.code:
            if not pattern_bit in self.code:
                return False
        return True


class DigitalNumber:
    def __init__(self, number, signal_pattern):
        self.number = number
        self.signal_pattern = signal_pattern if signal_pattern else ''

    def __str__(self):
        return f'[{self.number}]: {self.signal_pattern}'


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

    def get_sum_of_outputs(self):
        digital_outputs = self.get_digital_outputs()
        total = 0
        for x in digital_outputs:
            total += x
        return total

    def _print_digits(self):
        print(self.zero)
        print(self.one)
        print(self.two)
        print(self.three)
        print(self.four)
        print(self.five)
        print(self.six)
        print(self.seven)
        print(self.eight)
        print(self.nine)

    def _decode_pattern(self, signal_pattern):
        if signal_pattern == self.zero.signal_pattern:
            return self.zero.number
        if signal_pattern == self.one.signal_pattern:
            return self.one.number
        if signal_pattern == self.two.signal_pattern:
            return self.two.number
        if signal_pattern == self.three.signal_pattern:
            return self.three.number
        if signal_pattern == self.four.signal_pattern:
            return self.four.number
        if signal_pattern == self.five.signal_pattern:
            return self.five.number
        if signal_pattern == self.six.signal_pattern:
            return self.six.number
        if signal_pattern == self.seven.signal_pattern:
            return self.seven.number
        if signal_pattern == self.eight.signal_pattern:
            return self.eight.number
        if signal_pattern == self.nine.signal_pattern:
            return self.nine.number
        raise RuntimeError(f'Did we finish deduction?')

    def get_digital_outputs(self):
        digital_outputs = []
        for line in self.data:
            signal_pattern_strings = [SignalPattern(x).str for x in line[0]]
            self.set_pattern(signal_pattern_strings)
            # self._print_digits()
            encoded_outputs = line[1]
            decoded_array = [self._decode_pattern(SignalPattern(x)) for x in encoded_outputs]
            decoded_digit = int(''.join(str(n) for n in decoded_array))
            digital_outputs.append(decoded_digit)
            self.reset_numbers()
        return digital_outputs

    def set_pattern(self, signal_pattern_strings):
        # Get unique patterns first (1, 4, 7, 8)
        for pattern_string in signal_pattern_strings:
            signal_pattern = SignalPattern(pattern_string)
            self._set_unique_patterns(signal_pattern)
        signal_pattern_strings.remove(self.one.signal_pattern.str)
        signal_pattern_strings.remove(self.four.signal_pattern.str)
        signal_pattern_strings.remove(self.seven.signal_pattern.str)
        signal_pattern_strings.remove(self.eight.signal_pattern.str)

        # Next numbers that can be deduced are 3, 6
        for pattern_string in signal_pattern_strings:
            signal_pattern = SignalPattern(pattern_string)
            self._set_pattern_for_three_and_six(signal_pattern)
        signal_pattern_strings.remove(self.three.signal_pattern.str)
        signal_pattern_strings.remove(self.six.signal_pattern.str)

        # Next numbers that can be deduced are 0, 9
        for pattern_string in signal_pattern_strings:
            signal_pattern = SignalPattern(pattern_string)
            self._set_pattern_for_zero_and_nine(signal_pattern)
        signal_pattern_strings.remove(self.zero.signal_pattern.str)
        signal_pattern_strings.remove(self.nine.signal_pattern.str)

        # Last numbers to be deduced are 2, 5
        for pattern_string in signal_pattern_strings:
            signal_pattern = SignalPattern(pattern_string)
            # Number 5 will be found by checking number 9 contains 5's code
            if self.nine.signal_pattern.contains(signal_pattern):
                self.five = DigitalNumber(5, signal_pattern)
            # Number 2 is the remaining one
            else:
                self.two = DigitalNumber(2, signal_pattern)

    def _set_unique_patterns(self, signal_pattern):
        """Set unique pattern for 1, 4, 7, 8"""

        length_of_code = signal_pattern.length
        if length_of_code == MAP_PATTERNS[1]:
            self.one = DigitalNumber(1, signal_pattern)
        elif length_of_code == MAP_PATTERNS[4]:
            self.four = DigitalNumber(4, signal_pattern)
        elif length_of_code == MAP_PATTERNS[7]:
            self.seven = DigitalNumber(7, signal_pattern)
        elif length_of_code == MAP_PATTERNS[8]:
            self.eight = DigitalNumber(8, signal_pattern)

    def _set_pattern_for_three_and_six(self, signal_pattern):
        if signal_pattern.length == 5:
            # Number 3 is the only code length 5 that contains 1's code
            if signal_pattern.contains(self.one.signal_pattern):
                self.three = DigitalNumber(3, signal_pattern)
        elif signal_pattern.length == 6:
            # Number 6 is the only one code length 6 that does not contain 1's code
            if not signal_pattern.contains(self.one.signal_pattern):
                self.six = DigitalNumber(6, signal_pattern)

    def _set_pattern_for_zero_and_nine(self, signal_pattern):
        if signal_pattern.length == 6:
            # Number 9 contains 3's code
            if signal_pattern.contains(self.three.signal_pattern):
                self.nine = DigitalNumber(9, signal_pattern)
            # Number 0 is the other number
            else:
                self.zero = DigitalNumber(0, signal_pattern)


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
    output_sum = debug.get_sum_of_outputs()
    print(f'[!!] Sum of all digital outputs: {output_sum}')


main()
