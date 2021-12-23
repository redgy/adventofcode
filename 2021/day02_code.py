INPUT_FILEPATH="day02_input.txt"
# INPUT_FILEPATH="test_input.txt"


class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
        self.directives = self._parse_file()

    def _parse_file(self):
        directives = []
        with open(INPUT_FILEPATH, 'r') as f:
            data = f.readlines()
        for line in data:
            position, value = line.split(' ')
            entry = (position, int(value))
            directives.append(entry)
        return directives

    def perform_directives(self):
        for entry in self.directives:
            position = entry[0]
            value = entry[1]
            if position == 'forward':
                self.horizontal += value
                self.depth += (self.aim * value)
            elif position == 'down':
                self.aim += value
            elif position == 'up':
                self.aim -= value

    def calculate_product(self):
        self.perform_directives()
        print(f'( {self.horizontal}, '
                f'{self.depth}, '
                f'{self.aim} )')
        return self.horizontal * self.depth


def main():
    submarine = Submarine()
    return submarine.calculate_product()

print(main())
