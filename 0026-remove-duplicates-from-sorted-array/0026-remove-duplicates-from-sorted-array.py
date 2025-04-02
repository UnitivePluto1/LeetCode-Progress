class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        i = 1
        while(i<len(nums)):
            if nums[i] != nums[i-1]:       # to check for unique elements
                nums[j] = nums[i]
                j = j + 1
            i = i + 1
            
        return j

        