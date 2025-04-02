class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = 0
        temp = 0

        for right in range(k):
            temp+=nums[right]
        maxSum = temp
        for right in range(k, len(nums)):
            temp += nums[right]
            temp -= nums[right - k]
            maxSum = max(maxSum, temp)
        return maxSum/k