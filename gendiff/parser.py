import json
import yaml


def transform_value(value):
    '''Transforms boolean values to a propper format'''
    if isinstance(value, dict):
        return transform_bool(value)
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    else:
        return value


def transform_bool(_dict):
    '''Recursively ransforms bool values to strings with a proper format'''
    return {key: transform_value(value) for key, value in _dict.items()}


def parse_data(file_path):
    '''Parses data from both from JSON and YAML files'''
    try:
        with open(file_path, 'r') as file:
            if file_path.endswith('.json'):
                data = json.load(file)
            elif file_path.endswith(('.yaml', '.yml')):
                data = yaml.safe_load(file)
            else:
                raise ValueError(
                    'Invalid file type, must be .json or .yaml (.yml) file'
                )
        return data

    except FileNotFoundError:
        print(f'File not found: {file_path}')
        raise
