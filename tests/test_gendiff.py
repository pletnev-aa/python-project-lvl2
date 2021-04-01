import os
from gendiff.gendiff import generate_diff
from gendiff import parse


def test_json():
    current_dir = os.path.dirname(__file__)
    file1 = os.path.join(current_dir, 'fixtures/file1.json')
    file2 = os.path.join(current_dir, 'fixtures/file2.json')
    expected_answer = open(os.path.join(current_dir, 'fixtures/expected.txt'))
    expected = expected_answer.read()
    data_file1 = parse.get_data(file1)
    data_file2 = parse.get_data(file2)
    assert generate_diff(data_file1, data_file2) == expected


def test_yml():
    current_dir = os.path.dirname(__file__)
    file1 = os.path.join(current_dir, 'fixtures/file1.yml')
    file2 = os.path.join(current_dir, 'fixtures/file2.yml')
    expected_answer = open(os.path.join(current_dir, 'fixtures/expected.txt'))
    expected = expected_answer.read()
    data_file1 = parse.get_data(file1)
    data_file2 = parse.get_data(file2)
    assert generate_diff(data_file1, data_file2) == expected
