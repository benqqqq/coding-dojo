from math import log, ceil


def visualize_binary_tree(node_list):
    print('\n')
    print(str(node_list))
    print('--- draw ----')

    NODE_SPACE = 2

    height = ceil(log(len(node_list), 2))

    for i in range(0, height):
        start_index = pow(2, i) - 1
        local_width = pow(2, i)

        row_present = ' ' * NODE_SPACE * count_left_node(node_list, start_index)

        for j in range(start_index, min(start_index + local_width, len(node_list))):
            node_present = str(node_list[j]) if node_list[j] else 'x'
            row_present += ' ' * NODE_SPACE * (height - i) + node_present

        print(row_present)


"""
find the left space of a node
    travel the node and find how many left node in its children
"""


def count_left_node(nodes, index):
    left_index = index * 2 + 1

    if not _has_node(nodes, left_index):
        return 0

    return count_left_node(nodes, left_index) + 1


def _has_node(nodes, index):
    if index >= len(nodes):
        return False
    if nodes[index] is None:
        return False
    return True
