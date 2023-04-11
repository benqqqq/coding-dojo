from tools.binary_tree_visualization import count_left_node, visualize_binary_tree


def test_count_left_node():
    assert count_left_node([], 0) == 0
    assert count_left_node([1], 0) == 0
    assert count_left_node([1, 2], 0) == 1
    assert count_left_node([1, 2, 2, 3, 3, None, None, 4, 4], 0) == 3


def test_visualize_binary_tree():
    visualize_binary_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    visualize_binary_tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
