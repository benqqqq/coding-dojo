from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        product = 1
        for i in range(1, len(nums)):
            product *= nums[len(nums) - i]
            result[len(nums) - 1 - i] *= product

        return result
