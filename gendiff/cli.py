#!/usr/bin/env python3
import argparse
from gendiff import parse


def get_files():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Generate diff',
                                     usage='%(prog)s [-h] [-f FORMAT] first_file second_file')  # noqa: E501
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()  # noqa: F841
    first_file = args.first_file
    second_file = args.second_file
    return parse.get_data(first_file), parse.get_data(second_file)
