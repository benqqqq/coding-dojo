from solution import MinStack


def test_init_min_stack():
    MinStack()


def test_push_and_top():
    stack = MinStack()
    stack.push(1)
    assert stack.top() == 1

    stack.push(2)
    assert stack.top() == 2


def test_push_and_pop():
    stack = MinStack()
    stack.push(1)
    assert stack.pop() == 1
    assert stack.size == 0

    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.size == 1


def test_get_min():
    stack = MinStack()
    stack.push(-2)
    assert stack.getMin() == -2
    stack.push(-1)
    assert stack.getMin() == -2
    stack.push(-3)
    assert stack.getMin() == -3
    stack.pop()
    assert stack.getMin() == -2
    stack.pop()
    assert stack.getMin() == -2


def test_get_min_with_duplicated_element():
    stack = MinStack()
    stack.push(-2)
    stack.push(-3)
    stack.push(-3)
    assert stack.getMin() == -3
    stack.pop()
    assert stack.getMin() == -3
    stack.pop()
    assert stack.getMin() == -2
    stack.pop()
    # no element
    stack.push(-1)
    assert stack.getMin() == -1
