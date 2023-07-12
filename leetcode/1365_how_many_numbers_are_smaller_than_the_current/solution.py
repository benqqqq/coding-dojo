from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        mapping = {}
        sorted_nums = sorted(nums)

        # the first element doesn't have anyone is smaller than it
        mapping[sorted_nums[0]] = 0
        previous_num = sorted_nums[0]

        for i in range(1, len(sorted_nums)):
            num = sorted_nums[i]

            # if number is changed, means we can calculate how many elements is smaller than it
            if num != previous_num:
                mapping[num] = i
                previous_num = num
                continue

        return [mapping[num] for num in nums]
