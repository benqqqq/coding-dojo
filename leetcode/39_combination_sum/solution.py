from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current_candidates = []
        candidates = sorted(candidates)
        find_combination(candidates, target, current_candidates, result)
        return result


def find_combination(candidates, target, current_candidates, result):
    if target == 0:
        result.append(current_candidates)
        return

    if target < 0:
        return

    for candidate in candidates:
        if current_candidates and candidate < current_candidates[-1]:
            continue

        find_combination(
            candidates,
            target - candidate,
            [*current_candidates, candidate],
            result
        )





"""
2 3 6 7
target 7

2 2 3
7


[2,3,6,7](7)

[ ] + [3,6,7](7)
[2, ] +  [2,3,6,7](5)
[2,2, ] + [2,3,6,7](3)


for candidate in candidates:





"""
