from pprint import PrettyPrinter


def get_file_contents(filename: str, content_type="string") -> list:
    with open(filename, 'r') as f:
        data = f.readlines()
    return clean_list(data)


def clean_list(some_list: list) -> list:
    return [x.strip() for x in some_list if x]


def convert_str_to_int(character: str) -> int:
    try:
        number = int(character)
    except ValueError as e:
        raise(e)
    return number


def plog(contents: str):
    """Pretty print/log"""
    pp = PrettyPrinter(indent=2)
    pp.pprint(contents)
