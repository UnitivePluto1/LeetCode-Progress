class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq,ans=Counter(nums),0
        for x in freq: 
            if x+1 in freq: ans=max(ans, freq[x]+freq[x+1])
        return ans