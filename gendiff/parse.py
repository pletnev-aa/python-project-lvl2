import yaml


def get_data(file):
    data_file = yaml.safe_load(read(file))
    return data_file


def read(file):
    with open(file, 'r') as data:
        data_file = data.read()
        return data_file
