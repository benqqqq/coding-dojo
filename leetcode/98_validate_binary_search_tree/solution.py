from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return dfs_check_is_valid(root, lower_bound=-(2**31) - 1, upper_bound=2**31 + 1)


def dfs_check_is_valid(root: TreeNode, lower_bound: int, upper_bound: int) -> bool:
    if root.val <= lower_bound:
        return False

    if root.val >= upper_bound:
        return False

    if root.left and not dfs_check_is_valid(root.left, lower_bound, min(upper_bound, root.val)):
        return False

    if root.right and not dfs_check_is_valid(root.right, max(lower_bound, root.val), upper_bound):
        return False

    return True
