import argparse


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
    args = {
        'data1': args.first_file,
        'data2': args.second_file,
        'formatter': args.format,
    }
    return args
