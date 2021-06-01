import yaml
import json

ENTITY = [
    'data1',
    'data2',
    'formatter',
]
FILE_FORMATS = {
    'json': 'json',
    'yaml': 'yaml',
    'yml': 'yaml',
}


def get_data(args):
    data1, data2, formatter = args
    data1 = read(data1)
    data2 = read(data2)
    return dict(zip(ENTITY, (data1, data2, formatter)))


def read(data):
    form = data.rsplit('.', 1)[-1]
    if form == 'json':
        return json.load(open(data))
    elif form == 'yml' or form == 'yaml':
        return yaml.safe_load(open(data))
    else:
        raise NameError(
            'Wrong input data format. Can use only .json or .yml/.yaml'
        )
