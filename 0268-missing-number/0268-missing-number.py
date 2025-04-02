class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        v = [-1] * (n+1)
        for i in nums:
            v[i] = i
        for i in range(len(v)):
            if v[i] == -1:
                return i
        return 0
                