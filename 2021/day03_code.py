INPUT_FILEPATH="day03_input.txt"
class Submarine:
    def __init__(self):
        self.raw_data = self._parse_file()
        self.binary_dict = self.populate_dict(self.raw_data)
        self.gamma = -1
        self.epsilon = -1
        self.oxygen = -1
        self.carbon_dioxide = -1

    def _parse_file(self):
        with open(INPUT_FILEPATH, 'r') as f:
            raw_data = f.readlines()
            raw_data = [x.strip() for x in raw_data]
        return raw_data

    def populate_dict(self, data):
        binary_length = len(data[0])
        binary_dict = {x:[] for x in range(binary_length)}
        for entry in data:
            binary_array = [x for x in entry]
            for index, digit in enumerate(binary_array):
                binary_dict[index].append(int(digit))
        binary_dict = self._convert_dict_to_bin(binary_dict)
        return binary_dict

    def _convert_dict_to_bin(self, binary_dict):
        for key, value in binary_dict.items():
            bit = self._determine_bit(value)
            binary_dict[key] = bit
        return binary_dict

    def _determine_bit(self, binary_array):
        sum_zero = 0
        sum_one = 0
        for x in binary_array:
            if x == 0:
                sum_zero += 1
            else:
                sum_one +=1
        return 0 if sum_zero > sum_one else 1

    def _flip_bit(self, num):
        return 0 if num == 1 else 1

    def _calculate_rates(self):
        gamma_binary = ''
        epsilon_binary = ''
        for key, value in self.binary_dict.items():
            gamma_binary += str(value)
            epsilon_binary += str(self._flip_bit(value))
        self.gamma = int(gamma_binary, 2)
        self.epsilon = int(epsilon_binary, 2)

    def get_power_consumption(self):
        self._calculate_rates()
        return self.gamma * self.epsilon

    def _get_oxygen(self):
        valid_values = self.raw_data
        binary_dict = self.populate_dict(valid_values)
        index = 0
        valid_values = self._get_o2(index, valid_values, binary_dict)
        oxygen_bin = valid_values[0]
        return int(oxygen_bin, 2)

    def _get_o2(self, index, valid_values, binary_dict):
        if len(valid_values) == 1:
            return valid_values
        binary_dict = self.populate_dict(valid_values)
        bit = binary_dict[index]
        valid_values = [x for x in valid_values if int(x[index]) == bit]
        return self._get_o2(index+1, valid_values, binary_dict)

    def _get_carbon_dioxide(self):
        valid_values = self.raw_data
        binary_dict = self.populate_dict(valid_values)
        index = 0
        valid_values = self._get_c02(index, valid_values, binary_dict)
        carbon_dioxide_bin = valid_values[0]
        return int(carbon_dioxide_bin, 2)

    def _get_c02(self, index, valid_values, binary_dict):
        if len(valid_values) == 1:
            return valid_values
        binary_dict = self.populate_dict(valid_values)
        bit = self._flip_bit(binary_dict[index])
        valid_values = [x for x in valid_values if int(x[index]) == bit]
        return self._get_c02(index+1, valid_values, binary_dict)

    def get_life_support(self):
        self.oxygen = self._get_oxygen()
        self.carbon_dioxide = self._get_carbon_dioxide()
        return self.oxygen * self.carbon_dioxide


def main():
    submarine = Submarine()
    power_consumption = submarine.get_power_consumption()
    life_support = submarine.get_life_support()
    print(f'[!!] {life_support}')


main()
