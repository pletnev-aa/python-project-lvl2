STRINGS = {
    'property': 'Property',
    'updated': 'was updated. From',
    'added': 'was added with value:',
    'deleted': 'was removed',
    'form': '\'{}\'',
}


def get_format(diff, path=''):
    tree = []
    for key in diff.keys():
        line = key if not path else '.'.join([path, key])
        format_line = '{}'.format(line)
        if 'changed' in diff[key].keys():
            tree.append(' '.join([
                STRINGS['property'],
                STRINGS['form'].format(format_line),
                STRINGS['updated'],
                to_string(diff[key]['changed'][0]),
                'to',
                to_string(diff[key]['changed'][1])
            ]))
        elif 'added' in diff[key].keys():
            tree.append(' '.join([
                STRINGS['property'],
                STRINGS['form'].format(format_line),
                STRINGS['added'],
                to_string(diff[key]['added'])
            ]))
        elif 'deleted' in diff[key].keys():
            tree.append(' '.join([
                STRINGS['property'],
                STRINGS['form'].format(format_line),
                STRINGS['deleted'],
            ]))
        elif 'nested' in diff[key].keys():
            tree.append(get_format(
                diff[key]['nested'],
                path=format_line,
            ))
    return '\n'.join(tree)


def to_string(node):
    values = {'True': 'true', 'False': 'false', 'None': 'null'}
    if not isinstance(node, dict):
        if str(node) in values.keys():
            return values[str(node)]
        elif isinstance(node, int):
            return '{}'.format(node)
        return STRINGS['form'].format(node)
    else:
        return '[complex value]'
