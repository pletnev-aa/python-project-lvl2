import json

import pytest
from gendiff import gendiff


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
])
def test_generate_diff(file1, file2, form, expected):
    with open(expected, 'r') as result:
        expected = result.read()
    assert gendiff.generate_diff(file1, file2, form) == expected


@pytest.mark.parametrize('file1,file2,form,expected', [
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
def test_generate_diff_json(file1, file2, form, expected):
    expected = json.loads(gendiff.read_file(expected))
    assert json.loads(gendiff.generate_diff(file1, file2, form)) == expected
