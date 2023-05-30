from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 0, 1, 2 -> red, white, blue
        RED = 0
        WHITE = 1
        BLUE = 2

        red_i = 0
        white_i = 0
        blue_i = len(nums) - 1

        def swap(nums, i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while white_i <= blue_i:
            if nums[white_i] == RED:
                swap(nums, red_i, white_i)
                red_i += 1
                white_i += 1
            elif nums[white_i] == WHITE:
                white_i += 1
            elif nums[white_i] == BLUE:
                swap(nums, white_i, blue_i)
                blue_i -= 1


"""
r
w                   
                         b
--------------------------
 w
  w
   r
    b
    
   
"""
