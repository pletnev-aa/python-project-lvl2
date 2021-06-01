import yaml
import json
import argparse


ENTITY = [
    'file1',
    'file2',
    'formatter',
]


def get_args():
    description = 'Generate the difference between the two data structures.' \
                  ' Formation of the report in the form: plain, stylish, json'
    usage = '%(prog)s [-h] [-f FORMAT] first_file second_file'
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description=description,
                                     usage=usage)
    parser.add_argument('first_file',
                        help='enter the first file format: JSON, YAML or YML'
                        )
    parser.add_argument('second_file',
                        help='enter the second file format: JSON, YAML or YML'
                        )
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output: stylish, plain or json'
    )
    args = parser.parse_args()  # noqa: F841
    first_file = read_arg(args.first_file)
    second_file = read_arg(args.second_file)
    formatter = args.format
    return dict(zip(ENTITY, (first_file, second_file, formatter)))


def read_arg(file):
    form = file.rsplit('.', 1)[-1]
    if form == 'json':
        return json.load(open(file))
    elif form == 'yml' or form == 'yaml':
        return yaml.safe_load(open(file))
    else:
        raise NameError(
            'Wrong file format. Can use only .json or .yml/.yaml files'
        )
