import yaml
import json


def get_data(node):
    form = node.rsplit('.', 1)[-1]
    data = {}
    if form == 'json':
        data = json.load(open(node))
    elif form == 'yml':
        with open(node, 'r') as data_node:
            data = yaml.safe_load(data_node.read())
    return data
