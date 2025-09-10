class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for val in nums:
            if i<2 or val>nums[i-2]:
                nums[i]= val
                i+=1
            
        return i