"""
2399. Check Distances Between Same Letters
You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears exactly twice. You are also given a 0-indexed integer array distance of length 26.
Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).
In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i]. If the ith letter does not appear in s, then distance[i] can be ignored.
Return true if s is a well-spaced string, otherwise return false.
Example 1:
Input: s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: true
"""


class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        for i in range(len(s)):
            print(len(s))
            print(s[i+1].index(s[i]))
            try:
                if s[i+1].index(s[i]) != distance[ord(s[i])-97]:
                    return False
            except: pass
        return True


mysol = Solution()
mysol.checkDistances(s = "abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzza", distance = [49,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])