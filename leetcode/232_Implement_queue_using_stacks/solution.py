class MyQueue:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
        self.push_stack_front = None

    def push(self, x: int) -> None:
        if not self.push_stack:
            self.push_stack_front = x

        self.push_stack.append(x)

    def pop(self) -> int:
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())

        return self.pop_stack.pop()

    def peek(self) -> int or None:
        if self.pop_stack:
            return self.pop_stack[-1]
        if self.push_stack:
            return self.push_stack_front
        return None

    def empty(self) -> bool:
        return not self.push_stack and not self.pop_stack

    def __repr__(self):
        repr_stack = list(reversed(self.pop_stack)) + self.push_stack
        return str(repr_stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
