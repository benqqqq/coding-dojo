
memo = {}


def recursive_climb(n: int) -> int:
    if n in memo:
        return memo[n]

    if n == 0:
        solution = 1
    elif n == 1:
        solution = recursive_climb(n - 1)
    else:
        solution = recursive_climb(n - 1) + recursive_climb(n - 2)

    memo[n] = solution
    return solution


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        return recursive_climb(n)


class SolutionFromLeetCode:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        ways = [1, 2] + ([-1] * (n-2))

        for i in range(2, n):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n - 1]


"""
2 * m = n , m  n / 2        1

10 staircase to climb

1 & (n - 1)
    1 & (n -2)
    2 & (n -3)
2 & (n - 2)
    1 & (n -3)
    2 & (n -4)

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

2 * 0
[1, 2, 1, 1, ...] sum = n   1

2 * 1                       n-1
[1, 1, 1....]
[2, 1 ....]
[1 , 2 ...]

2 * 2

..
..

"""
