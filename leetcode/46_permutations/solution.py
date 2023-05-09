from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        generate_permutations(result, nums, [])
        return result


def generate_permutations(result: List[List[int]], nums: List[int], cur: List[int]) -> None:
    if not nums and cur:
        result.append(cur)

    for i in range(len(nums)):
        generate_permutations(
            result,
            nums[:i] + nums[i+1:],
            [*cur, nums[i]]
        )
