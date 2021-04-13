import os
from gendiff.gendiff import generate_diff
from gendiff import parse


CURRENT_DIR = os.path.dirname(__file__)
JSON_PLAIN1 = os.path.join(CURRENT_DIR, 'fixtures/file1.json')
JSON_PLAIN2 = os.path.join(CURRENT_DIR, 'fixtures/file2.json')
YML_PLAIN1 = os.path.join(CURRENT_DIR, 'fixtures/file1.yml')
YML_PLAIN2 = os.path.join(CURRENT_DIR, 'fixtures/file2.yml')
JSON_REC1 = os.path.join(CURRENT_DIR, 'fixtures/filepath1.json')
JSON_REC2 = os.path.join(CURRENT_DIR, 'fixtures/filepath2.json')
YML_REC1 = os.path.join(CURRENT_DIR, 'fixtures/filepath1.yml')
YML_REC2 = os.path.join(CURRENT_DIR, 'fixtures/filepath2.yml')
ANSWER = open(os.path.join(CURRENT_DIR, 'fixtures/answer.txt'))
ANSWER_REC = open(os.path.join(CURRENT_DIR, 'fixtures/answer_recursion.txt'))
ANSWER_PLAIN = open(os.path.join(CURRENT_DIR, 'fixtures/answer_plain.txt'))


def test_files():
    file1_json = parse.get_data(JSON_PLAIN1)
    file2_json = parse.get_data(JSON_PLAIN2)
    yml_file1 = parse.get_data(YML_PLAIN1)
    yml_file2 = parse.get_data(YML_PLAIN2)
    answer = ANSWER.read()
    assert generate_diff(file1_json, file2_json, 'stylish') == answer
    assert generate_diff(yml_file1, yml_file2, 'stylish') == answer


def test_recursion_files():
    answer = ANSWER_REC.read()
    answer_plain = ANSWER_PLAIN.read()
    file1_json = parse.get_data(JSON_REC1)
    file2_json = parse.get_data(JSON_REC2)
    yml_file1 = parse.get_data(YML_REC1)
    yml_file2 = parse.get_data(YML_REC2)
    assert generate_diff(file1_json, file2_json, 'stylish') == answer
    assert generate_diff(yml_file1, yml_file2, 'stylish') == answer
    assert generate_diff(file1_json, file2_json, 'plain') == answer_plain
    assert generate_diff(yml_file1, yml_file2, 'plain') == answer_plain
