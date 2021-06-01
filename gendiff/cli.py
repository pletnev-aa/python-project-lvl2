import yaml
import json
import argparse
from collections import defaultdict

FILE_FORMATS = {
    'json': 'json',
    'yaml': 'yaml',
    'yml': 'yaml',
}
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
    first_file = args.first_file
    second_file = args.second_file
    file_format = defaultdict(str)
    file_format[first_file] += first_file.rsplit('.', 1)[-1]
    file_format[second_file] += second_file.rsplit('.', 1)[-1]
    for key in file_format:
        if file_format[key] in FILE_FORMATS:
            first_file = read_arg(args.first_file, file_format[key])
            second_file = read_arg(args.second_file, file_format[key])
        else:
            raise ValueError(
                'Not file format: {}. '
                'Enter the file format: JSON, YAML, YML'.format(key)
            )
    formatter = args.format
    return dict(zip(ENTITY, (first_file, second_file, formatter)))


def read_arg(file, form):
    if form == 'json':
        with open(file) as data_file:
            return json.load(data_file)
    else:
        with open(file, 'r') as data_file:
            return yaml.safe_load(data_file.read())
