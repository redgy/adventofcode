from pprint import PrettyPrinter


def get_file_contents(filename: str, content_type="string") -> list:
    with open(filename, 'r') as f:
        data = f.readlines()
    return [x.strip() for x in data]


def plog(contents: str):
    """Pretty print/log"""
    pp = PrettyPrinter(indent=2)
    pp.pprint(contents)
