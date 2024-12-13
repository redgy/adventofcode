def read_txt(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data
