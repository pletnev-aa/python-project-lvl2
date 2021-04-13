TAB = '    '


def get_format(diff, tab=0):  # noqa: C901
    node = sorted(diff.keys())
    tree = []
    for child in node:
        if diff[child][0] == 'deleted':
            tree.append(get_line(
                tab,
                '  - ',
                child,
                walk(diff[child][1], tab + 1)
            ))
        elif diff[child][0] == 'added':
            tree.append(get_line(
                tab,
                '  + ',
                child,
                walk(diff[child][1], tab + 1)
            ))
        elif diff[child][0] == 'alike':
            tree.append(get_line(
                tab,
                TAB,
                child,
                walk(diff[child][1], tab + 1),
            ))
        elif diff[child][0] == 'changed':
            tree.append(get_line(
                tab,
                '  - ',
                child,
                walk(diff[child][1][0], tab + 1),
            ))
            tree.append(get_line(
                tab,
                '  + ',
                child,
                walk(diff[child][1][1], tab + 1),
            ))
        elif diff[child][0] == 'nested':
            tree.append(get_line(
                tab,
                TAB,
                child,
                get_format(diff[child][1], tab + 1),
            ))
    return '\n'.join([
        '{',
        *tree,
        '{}{}'.format(TAB * tab, '}'),
    ])


def get_line(indent, status, node, value):
    if not value:
        line = ''.join([indent * TAB, status, node, ':'])
        return ''.join([line, str(value)])
    line = ''.join([indent * TAB, status, node, ':'])
    return ' '.join([line, str(value)])


def walk(node, tab):
    items = {'True': 'true', 'False': 'false', 'None': 'null'}
    if not isinstance(node, dict):
        if str(node) in items.keys():
            return items[str(node)]
        return str(node)
    values = []
    for key in node.keys():
        values.append(''.join([
            TAB * (tab + 1),
            str(key),
            ': ',
            str(walk(
                node[key],
                tab + 1,
            )),
        ]))
    return '\n'.join([
        '{',
        *values,
        '{}{}'.format(TAB * tab, '}'),
    ])
