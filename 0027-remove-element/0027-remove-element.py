class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        j = 0
        i = 0
        while(i < len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j+=1
            i = i+1
        return j