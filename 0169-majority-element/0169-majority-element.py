class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashM = defaultdict(int)
        n = len(nums)

        for i in range(n):
            hashM[nums[i]] += 1
        
        n = n//2
        for k,v in hashM.items():
            if v > n:
                return k
        return 0
