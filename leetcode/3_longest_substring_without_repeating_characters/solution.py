from collections import defaultdict
from functools import reduce
from typing import Dict, List


def cal_char_index(s: str) -> Dict[str, List[int]]:
    mapping = defaultdict(list)
    for i, char in enumerate(s):
        mapping[char].append(i)
    return mapping


def cal_substring_length(char_index_mapping: Dict[str, List[int]], s_length: int) -> Dict[str, List[int]]:
    mapping = defaultdict(list)
    for char, indexes in char_index_mapping.items():
        if len(indexes) == 1:  # there is no repeat
            mapping[char].append(s_length)
            continue

        # first range
        # e.g. indexes = [0, 3], the substring is 0,1,2
        # e.g. indexes = [1, 3], the substring is 0,1,2
        mapping[char].append(indexes[1])

        # middle ranges
        # assume s_length is 8
        # e.g. indexes = [0, 3, 5], the substring is 1,2,3,4,5 (5=5-0)
        for i in range(0, len(indexes) - 2):
            mapping[char].append(indexes[i+2] - indexes[i])

        # final range
        # e.g. indexes = [0, 3], the substring is 1,2,3,4,5,6,7 (7=8-0-1)
        mapping[char].append(s_length - indexes[-2] - 1)

    return mapping


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_mapping = cal_char_index(s)
        substring_length_mapping = cal_substring_length(char_index_mapping, len(s))
        substring_length_list = reduce(lambda r, v: r + v, substring_length_mapping.values(), [])
        return min(substring_length_list)

    """
        seen      long      cur
        {}          0        0   
    d   {d}         0        1
    
    v   {d,v}       0        2
    
    d
    
    f
    
    dvdf
    
    26 + 10 + 25 + 1 ~= 50? = k
    
    a  |        |          |            m1
    b        |    |       |             m2
    c     |  
    find min m1 m2 , ...
    
    k * n
    
    0               4
    a   2, 4, 3         
    b   1, 5, 9
    c   ...
    d   0  2        ->  2   2
    e
    ...
    
    """


"""
dvdf

    d : 0, 2            
    v : 1
    f : 3

    d : 0, 2 -> -1, 0, 2, 4
  i  lower upper result 
  0   -1     2     2 - -1 - 1 = 2
  1   0     4      4 - 0 - 1 = 3
  2   break
  
  v : 1 -> -1, 0, 4
  0   -1  4   4 - -1 - 1 = 4
  
  f : 3 -> -1, 3, 4
   4

1,4,6,7

0~3    = 4 = 4 - 0
1~5    = 5 = 6 - 1
4~6    = 3 = 7 - 4
6~7    = 2 = 8 - 6



"""
