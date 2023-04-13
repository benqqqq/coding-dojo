from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs_tree(node: Optional[TreeNode], diameter: int) -> Tuple[int, int]:
            if not node:
                return 0, 0

            left_depth, left_diameter = dfs_tree(node.left, diameter)
            right_depth, right_diameter = dfs_tree(node.right, diameter)

            max_depth = max(left_depth, right_depth)
            diameter = max(left_diameter, right_diameter, left_depth + right_depth)

            return max_depth + 1, diameter

        result = dfs_tree(root, 0)
        return result[1]
