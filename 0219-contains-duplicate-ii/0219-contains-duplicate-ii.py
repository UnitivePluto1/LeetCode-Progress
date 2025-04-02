class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hMap = {}

        for i in range(len(nums)):
            if nums[i] in hMap:
                if i - hMap[nums[i]] <= k:
                    return True
                else: 
                    hMap[nums[i]] = i
            else:
                hMap[nums[i]] = i
        return False