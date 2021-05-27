STRINGS = {
    'tab': '    ',
    'added': '  + ',
    'deleted': '  - '
}


def get_stylish(diff, tab=0):
    tree = []
    for key in diff.keys():
        if 'deleted' in diff[key].keys():
            tree.append(get_line(
                tab,
                STRINGS['deleted'],
                key,
                to_string(diff[key]['deleted'], tab + 1)
            ))
        elif 'added' in diff[key].keys():
            tree.append(get_line(
                tab,
                STRINGS['added'],
                key,
                to_string(diff[key]['added'], tab + 1)
            ))
        elif 'alike' in diff[key].keys():
            tree.append(get_line(
                tab,
                STRINGS['tab'],
                key,
                to_string(diff[key]['alike'], tab + 1),
            ))
        elif 'changed' in diff[key].keys():
            tree.append(get_line(
                tab,
                STRINGS['deleted'],
                key,
                to_string(diff[key]['changed'][0], tab + 1),
            ))
            tree.append(get_line(
                tab,
                STRINGS['added'],
                key,
                to_string(diff[key]['changed'][1], tab + 1),
            ))
        else:
            tree.append(get_line(
                tab,
                STRINGS['tab'],
                key,
                get_stylish(diff[key]['nested'], tab + 1),
            ))
    return '\n'.join([
        '{',
        *tree,
        '{}{}'.format(STRINGS['tab'] * tab, '}'),
    ])


def get_line(indent, status, node, value):
    line = ''.join([indent * STRINGS['tab'], status, node, ':'])
    return ' '.join([line, str(value)])


def to_string(node, tab):
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
            str(to_string(
                node[key],
                tab + 1,
            )),
        ]))
    return '\n'.join([
        '{',
        *values,
        '{}{}'.format(STRINGS['tab'] * tab, '}'),
    ])
