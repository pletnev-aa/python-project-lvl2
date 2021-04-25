def get_format(diff, path=''):
    node = sorted(diff.keys())
    tree = []
    for key in node:
        line = key if not path else '.'.join([path, key])
        format_line = '{}'.format(line)
        if 'changed' in diff[key].keys():
            tree.append(' '.join([
                'Property',
                '\'{}\''.format(format_line),
                'was updated. From',
                walk(diff[key]['changed'][0]),
                'to',
                walk(diff[key]['changed'][1])
            ]))
        elif 'added' in diff[key].keys():
            tree.append(' '.join([
                'Property',
                '\'{}\''.format(format_line),
                'was added with value:',
                walk(diff[key]['added'])
            ]))
        elif 'deleted' in diff[key].keys():
            tree.append(' '.join([
                'Property',
                '\'{}\''.format(format_line),
                'was removed',
            ]))
        elif 'nested' in diff[key].keys():
            tree.append(get_format(
                diff[key]['nested'],
                path=format_line,
            ))
    return '\n'.join(tree)


def walk(node):
    values = {'True': 'true', 'False': 'false', 'None': 'null'}
    if not isinstance(node, dict):
        if str(node) in values.keys():
            return values[str(node)]
        return '\'{}\''.format(node)
    else:
        return '[complex value]'
