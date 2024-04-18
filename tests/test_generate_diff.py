import pytest
import os
import json
from gendiff import generate_diff
from gendiff.parser import parse_data


FIXTURES_DIR = os.path.join('tests', 'fixtures')


def get_file_path(filename):
    return os.path.join(FIXTURES_DIR, filename)


def load_txt(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data


@pytest.mark.parametrize('filename, filename_expected', [
    ('file1.json', 'file1.json'),
    ('file1.yaml', 'file1.json'),
    ('file2.json', 'file2.json'),
    ('file2.yaml', 'file2.json'),
])
def test_parse_data(filename, filename_expected):
    '''Tests data loading'''
    filepath = get_file_path(filename)
    filepath_expected = get_file_path(filename_expected)
    with open(filepath_expected, 'r') as f:
        dict_expected = json.load(f)
    assert parse_data(filepath) == dict_expected


@pytest.mark.parametrize('filename1, filename2, filename_expected', [
    ('file1.json', 'file2.json', 'expected12.txt'),
    ('file1.json', 'file1.json', 'expected11.txt'),
    ('file1.yaml', 'file2.json', 'expected12.txt'),
    ('file1.json', 'file1.yaml', 'expected11.txt'),
    ('nested1.json', 'nested2.json', 'nested_expected.txt'),
    ('nested1.yaml', 'nested2.yaml', 'nested_expected.txt'),
    ('nested1.yaml', 'nested2.json', 'nested_expected.txt'),
    ('nested1.json', 'nested2.yaml', 'nested_expected.txt')
])
def test_generate_diff(filename1, filename2, filename_expected):
    '''Tests basic behaviour'''
    filepath1 = get_file_path(filename1)
    filepath2 = get_file_path(filename2)
    filepath_expected = get_file_path(filename_expected)
    diff12 = generate_diff(filepath1, filepath2)
    expected_string = load_txt(filepath_expected)

    assert diff12 == expected_string


@pytest.mark.parametrize('filename1, filename2, filename_expected', [
    ('nested1.json', 'nested2.json', 'plain_expected.txt'),
    ('nested1.yaml', 'nested2.json', 'plain_expected.txt'),
    ('nested1.json', 'nested2.yaml', 'plain_expected.txt'),
    ('nested1.yaml', 'nested2.yaml', 'plain_expected.txt')
])
def test_generate_plain_diff(filename1, filename2, filename_expected):
    '''Tests basic behaviour with a plain formatter'''
    filepath1 = get_file_path(filename1)
    filepath2 = get_file_path(filename2)
    filepath_expected = get_file_path(filename_expected)
    diff12 = generate_diff(filepath1, filepath2, formatter='plain')
    expected_string = load_txt(filepath_expected)

    assert diff12 == expected_string


@pytest.mark.parametrize('filename1, filename2', [
    ('file1.json', 'nonexistent.json'),
    ('nonexistent.json', 'file1.json')
])
def test_generate_diff_robustness(filename1, filename2):
    '''Tests file reading errors handling'''
    filepath1 = get_file_path(filename1)
    filepath2 = get_file_path(filename2)

    with pytest.raises(FileNotFoundError):
        generate_diff(filepath1, filepath2)
