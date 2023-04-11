class Solution:
    def longestPalindrome(self, s: str) -> int:
        singular_characters = set()

        for c in s:
            if c in singular_characters:
                singular_characters.remove(c)
            else:
                singular_characters.add(c)

        if len(singular_characters) == 0:
            return len(s)
        return len(s) - len(singular_characters) + 1




"""
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

abccccdd
       dccaccd

"""