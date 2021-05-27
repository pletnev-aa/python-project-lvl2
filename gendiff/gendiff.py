from gendiff.formatter import format
from gendiff import parse


TYPES = {
    'added': 'added',
    'alike': 'alike',
    'changed': 'changed',
    'deleted': 'deleted',
    'nested': 'nested',
}


def generate_diff(file1, file2, formatter='stylish'):
    file1, file2 = parse.get_data(file1), parse.get_data(file2)
    diff = get_diff(file1, file2)
    return format.get_format(diff, formatter)


def get_diff(data1, data2):
    diff = {}
    node = sorted(data1.keys() & data2.keys())
    added_node = data2.keys() - data1.keys()
    deleted_node = data1.keys() - data2.keys()

    for key in node:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = {TYPES['nested']: get_diff(value1, value2)}
        elif value1 == value2:
            diff[key] = {TYPES['alike']: value1}
        else:
            diff[key] = {TYPES['changed']: (value1, value2)}
    for key in added_node:
        diff[key] = {TYPES['added']: data2[key]}
    for key in deleted_node:
        diff[key] = {TYPES['deleted']: data1[key]}
    return dict(sorted(diff.items()))
