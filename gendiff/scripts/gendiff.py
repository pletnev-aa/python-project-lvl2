#!/usr/bin/env python3
from gendiff.cli import get_files
from gendiff.gendiff import generate_diff


def main():
    return print(generate_diff(*get_files()))


if __name__ == '__main__':
    main()
