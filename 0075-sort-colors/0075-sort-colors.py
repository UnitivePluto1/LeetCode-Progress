class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        s = 0
        m = 0
        e = len(nums) - 1

        while m <= e:
            if nums[m] == 0:
                nums[s], nums[m] = nums[m], nums[s]
                s = s+1
                m = s
            elif nums[m] == 2:
                nums[e], nums[m] = nums[m], nums[e]
                e = e-1
            elif nums[m] == 1:
                m = m+ 1
        return nums
            
        
