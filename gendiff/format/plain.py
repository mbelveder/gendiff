def normalize(item):
    return flatten(item) if isinstance(item, list) else [item]


def flatten(tree):
    '''Flattens a nested list'''
    return sum(map(normalize, tree), [])


def get_nested(d: dict, keys: list):
    '''Gets a value from a nested list via absolute path'''
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key)
        else:
            return None
    return d


def get_value(d, keys):
    '''Postprocess a value obtained from the get_nested()'''
    value = get_nested(d, keys)
    if isinstance(value, (tuple, list, dict)):
        return '[complex value]'
    elif value in ['true', 'false', 'null'] or isinstance(value, (int, float)):
        return value
    else:
        return f"'{value}'"


def label_plain(dict1, dict2, ast_tree):
    '''Generates a plain diff representation'''

    change_types = {
        'added': "Property '{}' was added with value: {}",
        'deleted': "Property '{}' was removed",
        'changed': "Property '{}' was updated. From {} to {}",
    }

    def iter_(current_value, ancestry):
        if not isinstance(current_value, dict):
            ancestry_str = '.'.join(map(str, ancestry))
            if current_value in change_types:
                v1 = get_value(dict1, ancestry)
                v2 = get_value(dict2, ancestry)
                values_set = {
                    'added': [v2], 'deleted': [v1], 'changed': [v1, v2]
                }
                template = change_types[current_value]
                return template.format(
                    ancestry_str, *values_set.get(current_value)
                )
            else:
                return ''

        lines = []
        for key, val in current_value.items():
            new_ancestry = ancestry + [key]
            lines.append(iter_(val, new_ancestry))
        return lines

    return iter_(ast_tree, ancestry=[])


def plain(dict1, dict2, ast_tree):

    flat_plain = flatten(label_plain(dict1, dict2, ast_tree))
    # Filter out empty strings (unchanged values)
    flat_plain_format = [i for i in flat_plain if i]

    return '\n'.join(flat_plain_format)
