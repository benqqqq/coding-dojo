from priority_queue.code import PriorityQueue


class TestPriorityQueue:
    def test_empty_queue(self):
        queue = PriorityQueue()
        assert queue.extract_max() is None

    def test_queue_insert_1_element(self):
        queue = PriorityQueue()
        queue.insert(1)
        assert queue.extract_max() == 1

    def test_queue_insert_2_element(self):
        queue = PriorityQueue()
        queue.insert(2)
        queue.insert(1)
        assert queue.extract_max() == 2
