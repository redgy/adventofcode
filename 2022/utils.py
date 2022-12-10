import pprint
pp = pprint.PrettyPrinter(indent=2)


def get_basic_input(filename):
    """Basic input expected that requires no additional action besides a simple read in"""

    with open(filename, 'r') as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    return data


def get_input(filename, input_type='basic'):
    match input_type:
        case 'basic':
            return get_basic_input(filename)
        case _:
            raise ValueError(f'{input_type} not supported')


def print_results(results, blurb='look here'):
    print(blurb)
    print('-------')
    pp.pprint(results)
    print('')
