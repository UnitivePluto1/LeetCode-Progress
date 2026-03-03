class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        pSum = [0]
        for num in nums:
            pSum.append(num + pSum[-1])
        ans=[]
        for q in queries:
            idx=bisect.bisect(nums, q)
            ans.append(q*idx - pSum[idx] + (pSum[-1]-pSum[idx]) - q*(n-idx))
        return ans


        # nums = [2,4,3,1,6,9,5]  queries = [3,6] 

        # nums sort = [1,2,3,4,5,6,9] queries =[3,6]
        # pSum=[1,3,6,10,15,21,30]
        # for first q idx = 2, q = 3, ans =[]

        # q*idx (max value till index idx) - pSum[idx] (sum of all values till that index in this case) 
        # +
        # (pSum[-1] - pSum[idx])(current sum of all values from mid to end) - q*(n-idx)(max sum value for mid to end values)