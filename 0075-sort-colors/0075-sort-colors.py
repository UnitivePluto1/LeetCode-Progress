class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        beg = 0
        end = len(nums) - 1
        ind = 0

        while ind <= end:
            if nums[ind] == 0:
                nums[beg], nums[ind] = nums[ind],nums[beg]
                ind += 1
                beg += 1
            elif nums[ind] == 2:
                nums[end], nums[ind] = nums[ind], nums[end]
                end -= 1
            else:
                ind += 1