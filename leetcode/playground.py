# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        is_balanced, _ = find_is_balanced_or_not(root)
        return is_balanced


"""
output to the parent node : level and is balanced, if it is not balance, then break 
"""


def find_is_balanced_or_not(node):
    if not node:
        return True, 0

    left_node_is_balanced, left_node_level = find_is_balanced_or_not(node.left)
    right_node_is_balanced, right_node_level = find_is_balanced_or_not(node.right)

    is_balanced = abs(left_node_level - right_node_level) < 2 and left_node_is_balanced and right_node_is_balanced
    level = max(left_node_level, right_node_level) + 1

    return is_balanced, level
