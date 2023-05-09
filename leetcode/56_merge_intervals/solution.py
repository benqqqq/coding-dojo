from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda elem: elem[0])
        result = [sorted_intervals[0]]  # assume it must have 1 interval

        for i in range(1, len(sorted_intervals)):
            s, e = sorted_intervals[i]
            cs, ce = result[-1]
            if s <= ce:  # merge it
                result[-1][1] = max(ce, e)
            else:
                result.append([s, e])

        return result



"""

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

[[1,3],[2,6],[8,10],[15,18]] (10^4)

-------------------------------------
1   3 
  2.     6 
              8 10 
                      15       18
                          16 17

----------
               ---       
                       ------

sorted ? interveals
sort interval by its start

(ci)
current interval si === csi
current interval se === cse

start from intervals[0]

iterate 
    if si (start i) is inside ci, then we merge it , set cse = se
    else
        start a new interval




"""