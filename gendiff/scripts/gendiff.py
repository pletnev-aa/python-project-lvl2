#!/usr/bin/env python3
from gendiff.cli import get_args
from gendiff.gendiff import generate_diff


def main():
    data1, data2, formatter = get_args()
    return print(generate_diff(data1, data2, formatter))


if __name__ == '__main__':
    main()
