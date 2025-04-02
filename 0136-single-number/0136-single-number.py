class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       #i = 0
        #j = (len(nums) - 1)
        #flag = 0
        #while i < len(nums):
         #   if flag != 1 and j >= 0:
          #      if i == j:
           #         j-=1
            #    elif nums[i] == nums[j]:
             #       i+=1
              #      j=len(nums) - 1
               #     flag = 1
                #elif nums[i] != nums[j]:
                 #   j-=1
           # else:
            #    if flag == 1:
             #       flag = 0
              #  elif j < 0:
               #     return nums[i]
        xor = 0
        for i in nums:
            xor = xor^i
        return xor

            