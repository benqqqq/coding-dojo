class MinStack:
    def __init__(self):
        # store all the element
        self.stack = []
        # store only those minimum one at that time
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or self.getMin() >= val:
            self.min_stack.append(val)

    def pop(self) -> int | None:
        if not self.size:
            return None

        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        return self.stack.pop()

    def top(self) -> int | None:
        return self.stack[-1] if self.size else None

    def getMin(self) -> int | None:
        return self.min_stack[-1] if self.size else None

    @property
    def size(self):
        return len(self.stack)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



"""
[-2, 0, -3, 4, 5, 3] ....

getMin

-2      -2      [-2]  
0       -2      [-2]
-3      -3      [-2, -3]
4       -3      [-2, -3]
5       -3      [-2, -3]
3       -3      [-2, -3]

x3x     -3      [-2, -3]
x5x     -3      [-2, -3]
x4x     -3      [-2, -3]
x-3x    -2      [-2]
---

-2          [-2]
-1          [-2]
-3          [-2, -3]

x-3         [-2]
x-1         [-2]

--

-5          [-5]
-4          [-5]
-3          [-5]
-2  

-2
-3
---
-2          [-2]
-3          [-2, -3]
-2          [-2, -3]
-1          [-2, -3]
-3          [-2, -3, -3]
-4          [-2, -3, -3, -4]
-4          [-2, -3, -3, -4, -4]

x-4         [-2, -3, -3, -4]
x-4         [-2, -3, -3]

"""
