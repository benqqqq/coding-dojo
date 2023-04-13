# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_runner = head
        slow_runner = head

        while True:
            # assume fast_runner is not None
            if fast_runner.next is None:
                return slow_runner

            if fast_runner.next.next is None:
                return slow_runner.next

            fast_runner = fast_runner.next.next
            slow_runner = slow_runner.next


"""
 1 - 2 - 3 - 4 - 5 
         v
 
 #$
     #   $     
         #       $          faster->next is None     
                        
                             
 1 - 2 - 3 - 4 - 5 - 6
             V

#$
     #   $
         #       $          faster->next->next is None
            #            $
                        
"""
