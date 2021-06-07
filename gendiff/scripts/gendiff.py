#!/usr/bin/env python3
from gendiff.cli import get_args
from gendiff.gendiff import generate_diff


def main():
    return print(generate_diff(*get_args()))


if __name__ == '__main__':
    main()
