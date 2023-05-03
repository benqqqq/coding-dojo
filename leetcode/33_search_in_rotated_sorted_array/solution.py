from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        m = (s + e) // 2

        while s != e:
            if nums[m] == target:
                return m

            if nums[s] < nums[m]:  # pivot is not in left hand side
                if nums[s] <= target < nums[m]:  # regular binary search
                    e = m
                else:
                    s = m + 1
            else:  # pivot is not in right hand side
                if nums[m + 1] <= target <= nums[e]:  # regular binary search
                    s = m + 1
                else:
                    e = m

            m = (s + e) // 2

        return m if nums[m] == target else -1

# use two phase binary search may be better in readability
# phase 1 : find the pivot
# phase 2 : do binary search
