import os
from gendiff import gendiff


def test_answer():
    current_dir = os.path.dirname(__file__)
    file1 = os.path.join(current_dir, 'fixtures/file1.json')
    file2 = os.path.join(current_dir, 'fixtures/file2.json')
    expected_answer = open(os.path.join(current_dir, 'fixtures/expected.txt'))
    expected = expected_answer.read()
    result = gendiff.generate_diff(file1, file2)
    assert result == expected
