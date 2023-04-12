from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}

        # 5 nums -> 2,  6 nums -> 3
        half_of_nums = len(nums) // 2

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 0

            if counter[num] >= half_of_nums:
                return num
