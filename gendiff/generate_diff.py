from gendiff.parser import parse_data, transform_bool
from gendiff.format import plain, stylish


def sort_dict(d):
    sorted_dict = {}
    for k, v in sorted(d.items()):
        if isinstance(v, dict):
            sorted_dict[k] = sort_dict(v)
        else:
            sorted_dict[k] = v
    return sorted_dict


def generate_ast_diff(node1, node2):
    '''
    Generates a dictionary that shows the difference between to nested
    structures. This diff structure is separate from specific output,
    so the output format can alter.
    '''

    keys = node1.keys() | node2.keys()

    ast_tree = {}
    for key in keys:
        if key not in node1:
            ast_tree[key] = 'added'
        elif key not in node2:
            ast_tree[key] = 'deleted'
        elif node1[key] == node2[key]:
            ast_tree[key] = 'unchanged'
        # If both nodes are nested structures, treat it recursively
        elif isinstance(node1[key], dict) and isinstance(node2[key], dict):
            ast_tree[key] = generate_ast_diff(node1[key], node2[key])
        else:
            ast_tree[key] = 'changed'

    return ast_tree


def generate_diff(file_path1, file_path2, formatter='stylish'):
    '''Generates a difference between two nested json files'''

    dict1 = transform_bool(parse_data(file_path1))
    dict2 = transform_bool(parse_data(file_path2))

    ast_tree = sort_dict(generate_ast_diff(dict1, dict2))

    if formatter == 'stylish':
        return stylish(dict1, dict2, ast_tree)
    elif formatter == 'plain':
        return plain(dict1, dict2, ast_tree)
    elif formatter == 'json':
        return ast_tree
    else:
        raise ValueError(f"Invalid formatter: {formatter}")
