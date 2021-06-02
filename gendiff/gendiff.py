from gendiff.formatter import format
from gendiff.parse import read


TYPES = {
    'added': 'added',
    'alike': 'alike',
    'changed': 'changed',
    'deleted': 'deleted',
    'nested': 'nested',
}


def generate_diff(data1, data2, formatter='stylish'):  # noqa: C901
    def get_diff(input1, input2):
        diff = {}
        node = sorted(input1.keys() & input2.keys())
        added_node = input2.keys() - input1.keys()
        deleted_node = input1.keys() - input2.keys()
        for key in node:
            value1 = input1.get(key)
            value2 = input2.get(key)
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff[key] = {TYPES['nested']: get_diff(value1, value2)}
            elif value1 == value2:
                diff[key] = {TYPES['alike']: value1}
            else:
                diff[key] = {TYPES['changed']: (value1, value2)}
        for key in added_node:
            diff[key] = {TYPES['added']: input2[key]}
        for key in deleted_node:
            diff[key] = {TYPES['deleted']: input1[key]}
        return dict(sorted(diff.items()))
    return format.get_format(get_diff(read(data1), read(data2)), formatter)
