import json


def get_format(diff):
    for key in diff.keys():
        if isinstance(diff[key], dict) and 'nested' in diff[key]:
            diff[key] = diff[key]['nested']
            get_format(diff[key])
        elif 'changed' in diff[key]:
            keys = ['deleted', 'added']
            diff[key] = dict(zip(keys, diff[key]['changed']))
    return json.dumps(diff)
