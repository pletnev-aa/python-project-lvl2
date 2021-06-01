from gendiff.formatter import json
from gendiff.formatter import plain
from gendiff.formatter import stylish


FORMATS = {
    'plain': plain.get_plain,
    'json': json.get_json,
}


def get_format(diff, formatter):
    if formatter in FORMATS:
        return FORMATS[formatter](diff)
    else:
        return stylish.get_stylish(diff)
