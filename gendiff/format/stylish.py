def label_stylish(node1, node2, ast_node):
    '''
    Adds label to each node key base on the node value.
    First step in the `stylish` fomatter.
    '''

    keys = ast_node.keys()

    formatted_tree = {}
    for key in keys:
        if ast_node[key] == 'deleted':
            formatted_tree[f'- {key}'] = node1[key]
        elif ast_node[key] == 'added':
            formatted_tree[f'+ {key}'] = node2[key]
        elif ast_node[key] == 'unchanged':
            formatted_tree[f'{key}'] = node1[key]
        elif isinstance(ast_node[key], dict):
            formatted_tree[f'{key}'] = label_stylish(
                node1[key], node2[key], ast_node[key]
            )
        else:
            formatted_tree[f'- {key}'] = node1[key]
            formatted_tree[f'+ {key}'] = node2[key]

    return formatted_tree


def stringify(value, replacer=' ', spaces_count=4):
    '''
    Turns labelled dictionary to a properly formatted string.
    Second step in the `stylish` fomatter.
    '''

    if not isinstance(value, dict):
        return str(value)

    def walk(node, depth=1):
        indent = spaces_count * depth
        if not isinstance(node, dict):
            name = node[0]
            children = node[1]

            if name.startswith(('+', '-')):
                filler = replacer * (indent - 2)
            else:
                filler = replacer * indent

            if not isinstance(children, dict):
                item_str = filler + f'{name}: {children}'
            else:
                item_str = filler + f'{name}: {walk(children, depth + 1)}'

            return item_str

        formatted_strings = list(
            map(lambda node: walk(node, depth), node.items())
        )

        ending_filler = replacer * spaces_count * (depth - 1)
        formatted = '\n'.join(formatted_strings)
        return f"{{\n{formatted}\n{ending_filler}}}"

    return walk(value)


def stylish(dict1, dict2, ast_tree, replacer=' ', increment=4):

    labelled_diff = label_stylish(dict1, dict2, ast_tree)
    return stringify(labelled_diff, replacer, increment)
