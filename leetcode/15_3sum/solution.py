from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        result_map = set()

        for i in range(len(nums)):
            s = i + 1
            e = len(nums) - 1
            while s < e:
                nums_sum = nums[s] + nums[e] + nums[i]

                if nums_sum < 0:
                    s += 1
                elif nums_sum > 0:
                    e -= 1
                else:
                    result_key = f'{nums[i]}/{nums[s]}/{nums[e]}'
                    if result_key not in result_map:
                        result.append([nums[i], nums[s], nums[e]])
                        result_map.add(result_key)
                    s += 1

        return result






"""
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

[-1, 0, 1, 2, -1, -4]

Brute force

generate all possible combination of 3 triples
iterate each of them to find out if they are sum to 0
which will take O(combinations)
n numbers

        n * (n*-1) * (n*2)
(n 3) *  -------
        1 * 2 * 3

= O(n^3) = O(10^9) not accept
O(10^6)
better O(n^2)
3 * 10^3


[-1,

choose -> find the two of them equal to 1 in n-1 array

not choose -> find the three of them equal to 0 in n-1 array

     n
  a      b
c  d     e  f

...
1 1                         width of tree will be n


    1                    1 2^0  2^1 - 1
    2 3                  2      2^2 - 1
    4 5 6 7              4      2^3 - 1
8 9 10 11 12 13 14 16    8      2^d - 1 = n  n = 2^d + 1    d = log n


1 + 2 + 4 + 8 + ... 2^n

( 1 + 2^n ) * n / 2




            [1,2,3,4,5] 3

    [2,3,4,5] 2    [2,3,4,5] 3

[3,4,5] 1  [3,4,5] 2        [3,4,5] 2               [3,4,5] 3
         [4,5] 1  [4,5] 2     [4,5] 1 [4,5] 2


i   j   sum




"""
