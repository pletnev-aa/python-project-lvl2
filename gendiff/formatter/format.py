from gendiff.formatter import json
from gendiff.formatter import plain
from gendiff.formatter import stylish


FORMATS = {
    'stylish': stylish,
    'plain': plain,
    'json': json,
}


def format_diff(diff, formatter='stylish'):
    if formatter == 'json':
        return FORMATS[formatter].get_json(diff)
    elif formatter == 'plain':
        return FORMATS[formatter].get_plain(diff)
    else:
        return FORMATS[formatter].get_stylish(diff)
