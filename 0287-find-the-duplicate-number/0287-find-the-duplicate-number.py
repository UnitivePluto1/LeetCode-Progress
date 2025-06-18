class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
   #     for i in range(len(nums)):
  #          for j in nums[len(nums)-1:i:-1]:
 #               if nums[i] ^ j == 0:
#                    return j   


        s = nums[0]
        f = nums[0]
        while True:
            s= nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        
        s2 = nums[0]
        while s2!=s:
            s= nums[s]
            s2 = nums[s2]
        return s
