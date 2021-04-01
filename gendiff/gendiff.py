#!/usr/bin/env python3


def generate_diff(first_data, second_data):
    diff = []
    keys = set(first_data.keys() | set(second_data.keys()))
    for key in keys:
        if key not in second_data.keys():
            diff.append(
                '  - {key}: {value}'.format(key=key, value=first_data[key])
            )
        elif key not in first_data.keys():
            diff.append(
                '  + {key}: {value}'.format(key=key, value=second_data[key])
            )
        elif first_data.get(key) == second_data.get(key):
            diff.append(
                '    {key}: {value}'.format(key=key, value=second_data[key])
            )
        elif key in first_data.keys() and second_data.keys():
            diff.append(
                '  - {key}: {value}'.format(key=key, value=first_data[key])
            )
            diff.append(
                '  + {key}: {value}'.format(key=key, value=second_data[key])
            )
    diff.sort(key=lambda i: i[4])
    return '\n'.join(['{', '\n'.join(diff), '}']).lower()
