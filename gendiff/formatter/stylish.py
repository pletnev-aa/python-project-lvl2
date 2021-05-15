STRINGS = {
    'tab': '    ',
    'added': '  + ',
    'deleted': '  - '
}


def get_format(diff, tab=0):
    tree = []
    for key in diff.keys():
        if 'deleted' in diff[key].keys():
            tree.append(get_line(
                tab,
                STRINGS['deleted'],
                key,
                walk(diff[key]['deleted'], tab + 1)
            ))
        elif 'added' in diff[key].keys():
            tree.append(get_line(
                tab,
                STRINGS['added'],
                key,
                walk(diff[key]['added'], tab + 1)
            ))
        elif 'alike' in diff[key].keys():
            tree.append(get_line(
                tab,
                STRINGS['tab'],
                key,
                walk(diff[key]['alike'], tab + 1),
            ))
        elif 'changed' in diff[key].keys():
            tree.append(get_line(
                tab,
                STRINGS['deleted'],
                key,
                walk(diff[key]['changed'][0], tab + 1),
            ))
            tree.append(get_line(
                tab,
                STRINGS['added'],
                key,
                walk(diff[key]['changed'][1], tab + 1),
            ))
        else:
            tree.append(get_line(
                tab,
                STRINGS['tab'],
                key,
                get_format(diff[key]['nested'], tab + 1),
            ))
    return '\n'.join([
        '{',
        *tree,
        '{}{}'.format(STRINGS['tab'] * tab, '}'),
    ])


def get_line(indent, status, node, value):
    line = ''.join([indent * STRINGS['tab'], status, node, ':'])
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
            STRINGS['tab'] * (tab + 1),
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
        '{}{}'.format(STRINGS['tab'] * tab, '}'),
    ])
