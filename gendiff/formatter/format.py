from gendiff.formatter import json
from gendiff.formatter import plain
from gendiff.formatter import stylish


FORMATS = {
    'stylish': stylish,
    'plain': plain,
    'json': json,
}


def get_format(diff, formatter):
    if formatter == 'json':
        return FORMATS[formatter].get_json(diff)
    elif formatter == 'plain':
        return FORMATS[formatter].get_plain(diff)
    else:
        return FORMATS[formatter].get_stylish(diff)
