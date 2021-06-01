import yaml
import json
from os import path


FILE_FORMATS = {
    'json': json.load,
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load,
}


def read(data):
    data = path.abspath(data)
    data_form = data.rsplit('.', 1)[-1]
    if data_form in FILE_FORMATS:
        return FILE_FORMATS[data_form](open(data))
    else:
        raise NameError(
            'Wrong input data format. Can use only .json or .yml/.yaml'
        )
