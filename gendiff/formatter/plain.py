def get_format(diff, path=''):
    node = sorted(diff.keys())
    tree = []
    for child in node:
        line = child if not path else '.'.join([path, child])
        format_line = '{}'.format(line)
        if diff[child][0] == 'changed':
            tree.append(' '.join([
                'Property',
                '\'{}\''.format(format_line),
                'was updated. From',
                walk(diff[child][1][0]),
                'to',
                walk(diff[child][1][1])
            ]))
        elif diff[child][0] == 'added':
            tree.append(' '.join([
                'Property',
                '\'{}\''.format(format_line),
                'was added with value:',
                walk(diff[child][1])
            ]))
        elif diff[child][0] == 'deleted':
            tree.append(' '.join([
                'Property',
                '\'{}\''.format(format_line),
                'was removed',
            ]))
        elif diff[child][0] == 'nested':
            tree.append(get_format(
                diff[child][1],
                path=format_line,
            ))
    return '\n'.join(tree)


def walk(node):
    items = {'True': 'true', 'False': 'false', 'None': 'null'}
    if not isinstance(node, dict):
        if str(node) in items.keys():
            return items[str(node)]
        return '\'{}\''.format(node)
    elif isinstance(node, str):
        return "'{}'".format(node)
    elif isinstance(node, dict):
        return '[complex value]'
    return '{}'.format(node)
