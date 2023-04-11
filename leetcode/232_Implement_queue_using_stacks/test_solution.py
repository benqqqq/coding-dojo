from solution import MyQueue


def test_solution():
    queue = MyQueue()

    assert str(queue) == '[]'

    queue.push(1)
    assert str(queue) == '[1]'

    queue.push(2)
    assert str(queue) == '[1, 2]'

    queue.push(3)
    assert str(queue) == '[1, 2, 3]'

    assert queue.peek() == 1

    assert queue.pop() == 1

    assert queue.peek() == 2

    assert queue.empty() is False

    assert queue.pop() == 2

    assert queue.pop() == 3

    assert queue.empty() is True
