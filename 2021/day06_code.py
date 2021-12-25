INPUT_FILEPATH="day06_input.txt"
INPUT_FILEPATH="test_input.txt"
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
    print(data.clean_data)


main()
