TAB = '    '


def get_format(diff, tab=0):
    node = sorted(diff.keys())
    tree = []
    for key in node:
        if 'deleted' in diff[key].keys():
            tree.append(get_line(
                tab,
                '  - ',
                key,
                walk(diff[key]['deleted'], tab + 1)
            ))
        elif 'added' in diff[key].keys():
            tree.append(get_line(
                tab,
                '  + ',
                key,
                walk(diff[key]['added'], tab + 1)
            ))
        elif 'alike' in diff[key].keys():
            tree.append(get_line(
                tab,
                TAB,
                key,
                walk(diff[key]['alike'], tab + 1),
            ))
        elif 'changed' in diff[key].keys():
            tree.append(get_line(
                tab,
                '  - ',
                key,
                walk(diff[key]['changed'][0], tab + 1),
            ))
            tree.append(get_line(
                tab,
                '  + ',
                key,
                walk(diff[key]['changed'][1], tab + 1),
            ))
        else:
            tree.append(get_line(
                tab,
                TAB,
                key,
                get_format(diff[key]['nested'], tab + 1),
            ))
    return '\n'.join([
        '{',
        *tree,
        '{}{}'.format(TAB * tab, '}'),
    ])


def get_line(indent, status, node, value):
    line = ''.join([indent * TAB, status, node, ':'])
    return ' '.join([line, str(value)])


def walk(node, tab):
    values = {'True': 'true', 'False': 'false', 'None': 'null'}
    if not isinstance(node, dict):
        if str(node) in values.keys():
            return values[str(node)]
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
