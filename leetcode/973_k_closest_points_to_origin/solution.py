import math
from typing import List, Tuple


class Heap:
    def __init__(self) -> None:
        """
        [2,3,4,5,7,8,9,10]
            2
          3  4
        5 7  8 9
        10
        left child = 2i+1
        right child = 2i+2
        """
        self.elements = []

    def add(self, val: float, context: tuple) -> None:
        """add it to the tail, and swap"""
        self.elements.append((val, context))

        # start from the tail
        i = len(self.elements) - 1

        while True:
            # find the parent
            parent_i = (i - 1) // 2
            if parent_i < 0:
                break

            element = self.elements[i]
            parent_element = self.elements[parent_i]

            if element[0] >= parent_element[0]:
                break

            self.elements[parent_i] = element
            self.elements[i] = parent_element
            i = parent_i

    def pop(self) -> Tuple[float, tuple]:
        """remove it from the top, and swap"""
        pop_element = self.elements[0]
        self.elements[0] = self.elements[-1]
        self.elements.pop(-1)
        i = 0
        while True:
            # find the child
            left_index = i * 2 + 1
            right_index = i * 2 + 2

            if left_index >= len(self.elements) and right_index >= len(self.elements):
                break

            if left_index >= len(self.elements):
                swap_index = right_index
            elif right_index >= len(self.elements):
                swap_index = left_index
            elif self.elements[left_index][0] < self.elements[right_index][0]:
                swap_index = left_index
            else:
                swap_index = right_index

            element = self.elements[i]
            swap_element = self.elements[swap_index]

            if element[0] <= swap_element[0]:
                break

            self.elements[i] = swap_element
            self.elements[swap_index] = element
            i = swap_index

        return pop_element


def cal_euclidean_distance(x: int, y: int) -> float:
    return math.sqrt(pow(x, 2) + pow(y, 2))


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = Heap()

        for point in points:
            x, y = point
            distance = cal_euclidean_distance(x, y)
            heap.add(distance, (x, y))

        result = []
        for i in range(k):
            _, context = heap.pop()
            result.append([context[0], context[1]])

        return result


"""


the brute force time would be O(10^8) , O(len(x) * len(y))
assume points.length is m
the best cast should be O(m)
    O(m^2) = O(10^8)

    O(m) ~ O(m log m)


1, 2, 3, 4, ... m

O(m)
d1, d2, ...     dm

sort (O m long m)
d3, d2, d5, ... dm

return the first k


min heap tree


        3
    /   \
 3      4
        /\
      5     8

depth of the tree would log m
add -> log m
m * log m

delete log m
k * log m <= m * log m

2 * m log m = m log m

Heap

* add()

* pop()

"""
