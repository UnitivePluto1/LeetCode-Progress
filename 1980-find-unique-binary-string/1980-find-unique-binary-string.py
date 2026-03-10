class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""
        for i, v in enumerate(nums):
            if v[i] == "1":
                ans+= "0"
            else:
                ans+="1"
        return ans