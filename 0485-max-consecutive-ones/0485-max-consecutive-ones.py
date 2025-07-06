class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxC = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                if maxC < count:
                    maxC = count
                count = 0
                continue
        if maxC < count:
                maxC = count
        return maxC
            