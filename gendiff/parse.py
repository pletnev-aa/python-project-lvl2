import yaml
import json


def get_data(file):
    form = file.rsplit('.', 1)[-1]
    if form == 'json':
        with open(file) as data_file:
            return json.load(data_file)
    else:
        with open(file, 'r') as data_file:
            return yaml.safe_load(data_file.read())
