from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0  # window left
        j = 0  # window right
        char_map = {}
        longest_length = 0

        while j < len(s):
            # move window left
            if s[j] in char_map and char_map[s[j]] >= i:
                i = char_map[s[j]] + 1
                continue

            # move window right
            char_map[s[j]] = j
            longest_length = max(longest_length, j - i + 1)
            j += 1

        return longest_length

"""
window scan
abcacbb
|||x
 ---x
   ---|

abcabcbb 

|||x        
{abc}
0 start -> 3

 ---x
{bca}
1 start -> 3
  ---x
{cab}
2 start -> 3
   -
   ...
 



"""
