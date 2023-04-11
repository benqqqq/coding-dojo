from typing import Optional


class Node:

    def __init__(self, val=None, next_node=None) -> None:
        self.val = val
        self.next_node = next_node


class Queue:

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def enqueue(self, val):
        if self.is_empty():
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next_node = Node(val)
            self.tail = self.tail.next_node

    def dequeue(self):
        if self.is_empty():
            return None
        
        val = self.head.val
        self.head = self.head.next_node
        return val

    def is_empty(self):
        return self.head is None


if __name__ ==  '__main__':
    q = Queue()
    assert q.dequeue() is None
    q.enqueue(1)  # Node(1)<h><t>
    q.enqueue(2)  # Node(1)<h> -> Node(2)<t>
    q.enqueue(3)  # Node(1)<h> -> Node(2) -> Node(3)<t>

    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
