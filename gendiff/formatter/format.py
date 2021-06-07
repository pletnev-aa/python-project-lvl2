from gendiff.formatter import json
from gendiff.formatter import plain
from gendiff.formatter import stylish


FORMATS = {
    'plain': plain.get_plain,
    'json': json.get_json,
    'stylish': stylish.get_stylish,
}


def get_format(diff, formatter):
    if formatter in FORMATS:
        return FORMATS[formatter](diff)
    raise KeyError('Unknown output format: {}. Set format of output: {}'.format(formatter, ', '.join(FORMATS)))
