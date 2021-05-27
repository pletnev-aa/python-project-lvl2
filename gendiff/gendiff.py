from gendiff.formatter import format
from gendiff import parse


TYPES = {
    'added': 'added',
    'alike': 'alike',
    'changed': 'changed',
    'deleted': 'deleted',
    'nested': 'nested',
}


def generate_diff(file1, file2, formatter):
    file1, file2 = parse.get_data(file1), parse.get_data(file2)
    diff = get_diff(file1, file2)
    return format.format_diff(diff, formatter)


def get_diff(data1, data2):
    diff = {}
    node = sorted(data1.keys() & data2.keys())
    added_node = data2.keys() - data1.keys()
    deleted_node = data1.keys() - data2.keys()

    for key in node:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            value = {'nested': get_diff(value1, value2)}
        elif value1 == value2:
            value = {'alike': value1}
        else:
            value = {'changed': (value1, value2)}
        diff[key] = value
    for key in added_node:
        value = {'added': data2[key]}
        diff[key] = value
    for key in deleted_node:
        value = {'deleted': data1[key]}
        diff[key] = value
    return dict(sorted(diff.items()))
