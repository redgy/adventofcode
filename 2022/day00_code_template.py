from utils import get_input
from utils import print_results

FILENAME = 'day00_input_sample.txt'
FILENAME = 'day00_input.txt'


def get_data():
    """Get data from input"""

    return get_input(FILENAME, 'basic')


def main():
    data = get_data()
    print_results(data)


if __name__ == '__main__':
    main()
