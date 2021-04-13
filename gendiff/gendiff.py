#!/usr/bin/env python3
from gendiff.formatter import stylish, plain

FORMATS = {
    'stylish': stylish,
    'plain': plain,
}


def generate_diff(first_data, second_data, formatter):
    diff = get_diff(first_data, second_data)
    return FORMATS[formatter].get_format(diff)


def get_diff(first_data, second_data):
    diff = {}
    node = sorted(first_data.keys() & second_data.keys())
    added_node = second_data.keys() - first_data.keys()
    deleted_node = first_data.keys() - second_data.keys()

    for child in added_node:
        value = ('added', second_data[child])
        diff[child] = value
    for child in deleted_node:
        value = ('deleted', first_data[child])
        diff[child] = value
    for child in node:
        value1 = first_data.get(child)
        value2 = second_data.get(child)
        if isinstance(value1, dict) and isinstance(value2, dict):
            value = ('nested', get_diff(value1, value2))
        elif value1 == value2:
            value = ('alike', value1)
        else:
            value = ('changed', (value1, value2))
        diff[child] = value
    return diff
