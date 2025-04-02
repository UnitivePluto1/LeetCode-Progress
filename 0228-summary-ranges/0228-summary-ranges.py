class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0

        while i < len(nums):
            beg = nums[i]

            while i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
                i += 1
            
            if beg == nums[i]:
                ans.append(str(beg))
            else: 
                ans.append(str(beg) + "->" + str(nums[i]))
            i += 1
        return ans