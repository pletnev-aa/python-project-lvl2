import argparse
from gendiff import parse


def get_files():
    description = 'Generate the difference between the two data structures.' \
                  ' Formation of the report in the form: plain, stylish, json'
    usage = '%(prog)s [-h] [-f FORMAT] first_file second_file'
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description=description,
                                     usage=usage)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='Set format of output'
    )
    args = parser.parse_args()  # noqa: F841
    first_file = args.first_file
    second_file = args.second_file
    formatter = args.format
    return parse.get_data(first_file), parse.get_data(second_file), formatter
