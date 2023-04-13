# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return dfs(root)


def dfs(node: Optional[TreeNode]):
    if node is None:
        return 0
    return max(dfs(node.left), dfs(node.right)) + 1
