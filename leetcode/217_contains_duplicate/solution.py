from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicated_set = set()
        for num in nums:
            if num in duplicated_set:
                return True
            duplicated_set.add(num)

        return False
