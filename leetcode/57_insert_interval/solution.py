from typing import List



class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for i, interval in enumerate(intervals):
            if is_in_range(newInterval, interval):
                return intervals
            if is_overlapping(newInterval, interval):
                merged_interval = merge_interval(newInterval, interval)
                return insert_merged_interval(i, merged_interval, intervals)
            if is_passed_interval(newInterval, interval):
                return intervals[:i] + [newInterval] + intervals[i:]
        return intervals + [newInterval]


def is_in_range(new_interval: List[int], interval: List[int]) -> bool:
    """
    in_range visualization
    new_interval   <           >
    interval     <                  >
    """
    return interval[0] <= new_interval[0] and interval[1] >= new_interval[1]


def is_overlapping(new_interval: List[int], interval: List[int]) -> int:
    """
    in_range visualization
    new_interval   <           >            <           >     <  >
    interval           <          >       <      >          <       >
    """
    return (new_interval[0] <= interval[0] <= new_interval[1]) or (interval[0] <= new_interval[0] <= interval[1])


def merge_interval(new_interval: List[int], interval: List[int]) -> List[int]:
    start = min(new_interval[0], interval[0])
    end = max(new_interval[1], interval[1])
    return [start, end]


def insert_merged_interval(i: int, merged_interval: List[int], intervals: List[List[int]]) -> List[List[int]]:
    merged_intervals = intervals[:i]
    merged_interval_inserted = False

    for interval in intervals[i + 1:]:
        if is_in_range(interval, merged_interval):
            continue  # drop interval
        if is_overlapping(interval, merged_interval):
            merged_interval = merge_interval(interval, merged_interval)
            continue

        if not merged_interval_inserted:
            merged_intervals += [merged_interval]
            merged_interval_inserted = True

        merged_intervals += [interval]

    if not merged_interval_inserted:
        merged_intervals += [merged_interval]

    return merged_intervals


def is_passed_interval(new_interval: List[int], interval: List[int]):
    return new_interval[0] <= interval[0]


"""
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]


(10^5)
1 2 3 4 5 6 7 8 9 10 (10^4)
<   >     <     >
  <     >

<       > <     >


let n_s, n_e (2, 5)

for each interval O(n)
    i_s, i_e (1, 3)

    if newInterval is fully in range:
        if all the range is in local range
            do nothing, and return 
        if newInterval is partial in range:
            define new start and end
            modify the intervals
            return
    else:
        move to next

# the range should be at the last
insert into the last


"""
