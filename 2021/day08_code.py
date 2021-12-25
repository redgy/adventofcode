INPUT_FILEPATH="day08_input.txt"
INPUT_FILEPATH="test_input.txt"
class UniqueDigit:
    # 1, 4, 7, 8
    def __init__(self, number):
        if number == 1:
            self.unique_wires = 2
        elif number == 4:
            self.unique_wires = 4
        elif number == 7:
            self.unique_wires = 3
        elif number == 8:
            self.unique_wires = 7
        raise ValueError(f'{number} is not a unique digit')

class InputData:
    def __init__(self):
        self.raw_data = None
        self._parse_file()

    def _parse_file(self):
        with open(INPUT_FILEPATH, 'r') as f:
            raw_data = f.readlines()
        self.raw_data = [x.strip() for x in raw_data]


def main():
    data = InputData()
    print(f'[!!] {data.raw_data}')


main()
