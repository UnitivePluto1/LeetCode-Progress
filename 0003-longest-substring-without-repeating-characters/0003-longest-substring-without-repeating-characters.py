class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cs = set()
        start = 0
        maxi = 0

        for end in range(len(s)):
            while s[end] in cs:
                cs.remove(s[start])
                start += 1
            
            cs.add(s[end])
            maxi = max(maxi, end-start+1)
        return maxi

        