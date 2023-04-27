from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        # 0~0, 0~1, 0~2, ... 0~n-1
        product_from_left = [nums[0]]
        # n-1~n-1, n-2~n-1, n-3~n-1, ... 0~n-1
        product_from_right = [nums[nums_len - 1]]

        for i in range(1, nums_len):
            product_from_left.append(product_from_left[i - 1] * nums[i])

        for i in range(1, nums_len):
            product_from_right.append(product_from_right[i - 1] * nums[nums_len - 1 - i])

        result = []
        for i in range(nums_len):
            # if i === 3 , result = left[0~2] * right[4~n-1] = left[2] * right[-5]
            left = 1 if i == 0 else product_from_left[i - 1]
            right = 1 if i == (nums_len - 1) else product_from_right[-(i + 2)]
            result.append(left * right)

        return result
