class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
            
        max_s = s[0]
        for i in range(len(s)-1):
            odd = expand(i, i)
            even = expand(i, i+1)

            if len(odd) > len(max_s):
                max_s = odd
            if len(even) > len(max_s):
                max_s = even
    
        return max_s