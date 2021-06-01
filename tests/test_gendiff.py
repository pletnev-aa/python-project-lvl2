import json
import pytest
from gendiff import cli
from gendiff import gendiff


@pytest.mark.parametrize('file1,file2,file_form,form,expected', [
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'json',
     'stylish',
     'tests/fixtures/expected_stylish.txt'
     ),
    ('tests/fixtures/file1.yml',
     'tests/fixtures/file2.yml',
     'yml',
     'stylish',
     'tests/fixtures/expected_stylish.txt'
     ),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'json',
     'plain',
     'tests/fixtures/expected_plain.txt'
     ),
    ('tests/fixtures/file1.yml',
     'tests/fixtures/file2.yml',
     'yml',
     'plain',
     'tests/fixtures/expected_plain.txt'
     ),
    ('tests/fixtures/filepath1.json',
     'tests/fixtures/filepath2.json',
     'json',
     'stylish',
     'tests/fixtures/expected_stylish_rec.txt'
     ),
    ('tests/fixtures/filepath1.yml',
     'tests/fixtures/filepath2.yml',
     'yml',
     'stylish',
     'tests/fixtures/expected_stylish_rec.txt'
     ),
    ('tests/fixtures/filepath1.json',
     'tests/fixtures/filepath2.json',
     'json',
     'plain',
     'tests/fixtures/expected_plain_rec.txt'
     ),
    ('tests/fixtures/filepath1.yml',
     'tests/fixtures/filepath2.yml',
     'yml',
     'plain',
     'tests/fixtures/expected_plain_rec.txt'
     ),
])
def test_generate_diff(file1, file2, file_form, form, expected):
    file1 = cli.read_arg(file1, file_form)
    file2 = cli.read_arg(file2, file_form)
    result = gendiff.generate_diff(file1, file2, form)
    with open(expected, 'r') as data:
        expected = data.read()
    assert result == expected


@pytest.mark.parametrize('file1,file2,file_form,form,expected', [
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'json',
     'json',
     'tests/fixtures/expected.json'
     ),
    ('tests/fixtures/file1.yml',
     'tests/fixtures/file2.yml',
     'yml',
     'json',
     'tests/fixtures/expected.json'
     ),
    ('tests/fixtures/filepath1.json',
     'tests/fixtures/filepath2.json',
     'json',
     'json',
     'tests/fixtures/expected_recursion.json'
     ),
    ('tests/fixtures/filepath1.yml',
     'tests/fixtures/filepath2.yml',
     'yml',
     'json',
     'tests/fixtures/expected_recursion.json'
     ),
])
def test_generate_diff_json(file1, file2, file_form, form, expected):
    file1 = cli.read_arg(file1, file_form)
    file2 = cli.read_arg(file2, file_form)
    diff = gendiff.generate_diff(file1, file2, form)
    result = json.loads(diff)
    expected = cli.read_arg(expected, file_form)
    assert result == expected
