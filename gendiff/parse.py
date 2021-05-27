import yaml
import json


def get_data(file):
    form = file.rsplit('.', 1)[-1]
    if form == 'json':
        return json.load(open(file))
    elif form == 'yml' or form == 'yaml':
        return yaml.safe_load(open(file))
    else:
        raise NameError(
            'Wrong file format. Can use only .json or .yml/.yaml files'
        )
