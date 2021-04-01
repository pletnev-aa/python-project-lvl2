#!/usr/bin/env python3
import json


def generate_diff(file1, file2):
    diff = []
    file1 = json.load(open(file1))
    file2 = json.load(open(file2))
    keys = set(file1.keys() | set(file2.keys()))
    for key in keys:
        if key not in file2.keys():
            diff.append('  - {key}: {value}'.format(key=key, value=file1[key]))
        elif key not in file1.keys():
            diff.append('  + {key}: {value}'.format(key=key, value=file2[key]))
        elif file1.get(key) == file2.get(key):
            diff.append('    {key}: {value}'.format(key=key, value=file2[key]))
        elif key in file1.keys() and file2.keys():
            diff.append('  - {key}: {value}'.format(key=key, value=file1[key]))
            diff.append('  + {key}: {value}'.format(key=key, value=file2[key]))
    diff.sort(key=lambda i: i[4])
    return '\n'.join(['{', '\n'.join(diff), '}']).lower()
