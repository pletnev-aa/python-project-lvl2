#!/usr/bin/env python3
from gendiff.cli import get_args
from gendiff.gendiff import generate_diff
from gendiff import parse


def main():
    return print(generate_diff(**parse.get_data(get_args())))


if __name__ == '__main__':
    main()
