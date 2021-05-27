import yaml
import json


def get_data(file):
    form = file.rsplit('.', 1)[-1]
    with open(file) as data_file:
        if form == 'json':
            return json.load(data_file)
        else:
            return yaml.safe_load(data_file)
