# Definition for a binary tree node.


import queue
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = queue.Queue()
        q.put((root, 0))

        while not q.empty():
            node: TreeNode
            level: int
            node, level = q.get()

            # put next items into queue
            if node.left:
                q.put((node.left, level + 1))
            if node.right:
                q.put((node.right, level + 1))

            # output to result
            if not result:  # the first one result
                result.append([(node, level)])
                continue

            last_node: TreeNode
            last_level: int
            last_node, last_level = result[-1][-1]
            if level == last_level:  # at the same level, append to the last level result
                result[-1].append((node, level))
                continue

            result.append([(node, level)])  # at different level, start a new level result

        cleaned_result = []
        for level_result in result:
            cleaned_result.append([node.val for node, level in level_result])

        return cleaned_result
