# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# first attempt
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        reached = set()
        node = head

        while True:
            if not node:
                break

            if node in reached:
                return True

            reached.add(node)
            node = node.next

        return False


# try to reduce memory usage
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        TOUCHED_VALUE = 10**6  # -10**5 <= Node.val <= 10**5 , 10**6 is impossible to appear in the node

        while True:
            if not node:
                break

            if node.val == TOUCHED_VALUE:
                return True

            node.val = TOUCHED_VALUE
            node = node.next

        return False


