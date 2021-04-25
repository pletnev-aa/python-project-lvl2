import pytest
from gendiff.gendiff import generate_diff
from gendiff import parse


@pytest.mark.parametrize('file1,file2,form,expected', [
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'stylish',
     'tests/fixtures/expected_stylish.txt'
     ),
    ('tests/fixtures/file1.yml',
     'tests/fixtures/file2.yml',
     'stylish',
     'tests/fixtures/expected_stylish.txt'
     ),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'plain',
     'tests/fixtures/expected_plain.txt'
     ),
    ('tests/fixtures/file1.yml',
     'tests/fixtures/file2.yml',
     'plain',
     'tests/fixtures/expected_plain.txt'
     ),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'json',
     'tests/fixtures/expected.json'
     ),
    ('tests/fixtures/file1.yml',
     'tests/fixtures/file2.yml',
     'json',
     'tests/fixtures/expected.json'
     ),
])
def test_flat_files(file1, file2, form, expected):
    with open(expected, 'r') as result:
        expected = result.read()
    file1 = parse.get_data(file1)
    file2 = parse.get_data(file2)
    assert generate_diff(file1, file2, form) == expected


@pytest.mark.parametrize('file1,file2,form,expected', [
    ('tests/fixtures/filepath1.json',
     'tests/fixtures/filepath2.json',
     'stylish',
     'tests/fixtures/expected_stylish_rec.txt'
     ),
    ('tests/fixtures/filepath1.yml',
     'tests/fixtures/filepath2.yml',
     'stylish',
     'tests/fixtures/expected_stylish_rec.txt'
     ),
    ('tests/fixtures/filepath1.json',
     'tests/fixtures/filepath2.json',
     'plain',
     'tests/fixtures/expected_plain_rec.txt'
     ),
    ('tests/fixtures/filepath1.yml',
     'tests/fixtures/filepath2.yml',
     'plain',
     'tests/fixtures/expected_plain_rec.txt'
     ),
    ('tests/fixtures/filepath1.json',
     'tests/fixtures/filepath2.json',
     'json',
     'tests/fixtures/expected_recursion.json'
     ),
    ('tests/fixtures/filepath1.yml',
     'tests/fixtures/filepath2.yml',
     'json',
     'tests/fixtures/expected_recursion.json'
     ),
])
def test_recursion_files(file1, file2, form, expected):
    with open(expected, 'r') as result:
        expected = result.read()
    file1 = parse.get_data(file1)
    file2 = parse.get_data(file2)
    assert generate_diff(file1, file2, form) == expected
