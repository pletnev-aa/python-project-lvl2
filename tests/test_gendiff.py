import json
import pytest
from gendiff import gendiff
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
    data = (file1, file2, form)
    result = gendiff.generate_diff(**parse.get_data(data))
    with open(expected) as data:
        expected = data.read()
    assert result == expected


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
    data = (file1, file2, form)
    result = json.loads(gendiff.generate_diff(**parse.get_data(data)))
    expected = parse.read(expected)
    assert result == expected
