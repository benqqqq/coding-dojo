class Queue:
    class FullException(Exception):
        pass

    def __init__(self, size: int) -> None:
        self.store = [None] * size
        self.size = size
        self.head = None
        self.tail = None
        self._reset_pointer()

    def _reset_pointer(self):
        self.head: int = -1
        self.tail: int = -1

    def enqueue(self, val):
        if self.is_full():
            raise self.FullException()

        if self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = self._next_tail()

        self.store[self.tail] = val

    def dequeue(self):
        if self.is_empty():
            return None

        val = self.store[self.head]
        self.head = self._next_head()

        if self.is_empty():
            self._reset_pointer()

        return val

    def is_empty(self):
        return self.head == -1 and self.tail == -1

    def is_full(self):
        return self._next_tail() == self.head

    def _next_head(self):
        return (self.head + 1) % self.size

    def _next_tail(self):
        return (self.tail + 1) % self.size


if __name__ == '__main__':
    q = Queue(size=3)
    assert q.dequeue() is None
    q.enqueue(1)  # Node(1)<h><t>
    q.enqueue(2)  # Node(1)<h> -> Node(2)<t>
    q.enqueue(3)  # Node(1)<h> -> Node(2) -> Node(3)<t>

    assert q.dequeue() == 1
    assert q.dequeue() == 2

    q.enqueue(4)

    assert q.dequeue() == 3
    assert q.dequeue() == 4
