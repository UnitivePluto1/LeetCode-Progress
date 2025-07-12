class Solution:
    def minDeletions(self, s: str) -> int:
        freq = [0]*26

        for i in s:
            freq[ord(i)-ord('a')] += 1
        freq.sort()

        cnt = 0

        for i in range(24,-1,-1):
            if freq[i] == 0:
                break
            if freq[i] >= freq[i+1]:
                temp = freq[i]
                freq[i] = max(0, freq[i+1]-1)
                cnt += temp - freq[i]
        return cnt
