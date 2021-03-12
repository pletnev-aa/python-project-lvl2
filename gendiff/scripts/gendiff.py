#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Generate diff',
                                     usage='%(prog)s [-h] [-f FORMAT] first_file second_file')  # noqa: E501
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()  # noqa: F841


if __name__ == '__main__':
    main()
