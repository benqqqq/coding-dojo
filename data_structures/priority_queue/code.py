
class PriorityQueue:

    def __init__(self) -> None:
        """
        complete binary tree
        [0,1,2,3,4,5,6,7]
             1
           2  3
         4  5 6  7
        """
        self.queue = [None]

    def extract_max(self):
        if len(self.queue) > 1:
            return self.queue[1]
        return None

    def insert(self, value):
        """put value into the last, swim"""
        self.queue.append(value)
        self._swim(len(self.queue))

    def _swim(self, index):
        current = self.queue[index]
        parent_index = index // 2
        if parent_index <= 0:
            return

        parent = self.queue[parent_index]
        if parent > current:
            return

        # switch
        self.queue[parent_index] = current
        self.queue[index] = parent
        self._swim(parent_index)
