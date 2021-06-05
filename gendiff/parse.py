import yaml
import json


FILE_FORMATS = {
    'json': json.loads,
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load,
}


def get_parse(data, form):
    if form in FILE_FORMATS:
        return FILE_FORMATS[form](data)
    else:
        raise NameError(
            'Wrong input data format. Can use only .json or .yml/.yaml'
        )


def read_file(filename):
    with open(filename, 'r') as data:
        return data.read()


def get_format(filename):
    return filename.rsplit('.', 1)[-1]
