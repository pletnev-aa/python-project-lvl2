import json


def get_format(diff):
    node = sorted(diff.keys())
    for key in node:
        if isinstance(diff[key], dict) and 'nested' in diff[key]:
            diff[key] = diff[key]['nested']
            get_format(diff[key])
        elif 'changed' in diff[key]:
            keys = ['deleted', 'added']
            values = [diff[key]['changed'][0], diff[key]['changed'][1]]
            diff[key] = dict(zip(keys, values))
    return json.dumps(diff, indent=2, sort_keys=True)