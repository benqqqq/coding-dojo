from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = nums[0]
        local_max = nums[0]

        for num in nums[1:]:
            # choose whether we should pick current one and abandon previous
            if num > (num + local_max):
                local_max = num
            else:
                local_max = num + local_max

            if local_max > global_max:
                global_max = local_max

        return global_max





"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

divide & conquer ?

[-2, 1, -3]
    [1, -3, 4, -1]

evidence
    - sum
    - subarray
    - bf -> O(n^2)
    - target -> O(n)
    - divide by different subarray, how to find the result that across them?
    - for each
                            so_far      end_here
        -2
            -2              -2              -2
        1
            -2+1=-1         1               -1
        -3
            -1+-3=-4        1
        4

        -1
        ...
"""

