from gendiff.formatter import stylish, plain, json
from gendiff import parse

FORMATS = {
    'stylish': stylish,
    'plain': plain,
    'json': json,
}


def generate_diff(first_data, second_data, formatter='stylish'):
    first_data = parse.get_data(read_file(first_data), get_format(first_data))
    second_data = parse.get_data(read_file(second_data), get_format(second_data))  # noqa: E501
    diff = get_diff(first_data, second_data)
    return FORMATS[formatter].get_format(diff)


def get_format(file):
    return file.rsplit('.', 1)[-1]


def read_file(file):
    with open(file, 'r') as data:
        data_file = data.read()
    return data_file


def get_diff(first_data, second_data):
    diff = {}
    node = sorted(first_data.keys() & second_data.keys())
    added_node = second_data.keys() - first_data.keys()
    deleted_node = first_data.keys() - second_data.keys()

    for key in node:
        value1 = first_data.get(key)
        value2 = second_data.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            value = {'nested': get_diff(value1, value2)}
        elif value1 == value2:
            value = {'alike': value1}
        else:
            value = {'changed': (value1, value2)}
        diff[key] = value
    for key in added_node:
        value = {'added': second_data[key]}
        diff[key] = value
    for key in deleted_node:
        value = {'deleted': first_data[key]}
        diff[key] = value
    return dict(sorted(diff.items()))
