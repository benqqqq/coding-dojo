class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Example 1:

        Input: ransomNote = "a", magazine = "b"
        Output: false
        Example 2:

        Input: ransomNote = "aa", magazine = "ab"
        Output: false
        Example 3:

        Input: ransomNote = "aa", magazine = "aab"
        Output: true
        {
            a: 2
            b: 1
        }
        time : O(n) , space : O(n)
        iterate ransom Note, each time, consume 1 character, if ran out of character, then fail
        time : O(n)
        """
        magazine_map = {}
        for c in magazine:
            if c in magazine_map:
                magazine_map[c] += 1
            else:
                magazine_map[c] = 1

        for c in ransomNote:
            if magazine_map.get(c, 0) == 0:
                return False

            magazine_map[c] -= 1

        return True
