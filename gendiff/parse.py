import yaml
import json


def get_data(file, form):
    data = {}
    if form == 'json':
        data = json.loads(file)
    elif form == 'yml' or form == 'yaml':
        data = yaml.safe_load(file)
    return data
