class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        arr = []
        ans = []

        for i, num in enumerate(nums):
            if num == x:
                arr.append(i)
        
        for q in queries:
            if len(arr) < q:
                ans.append(-1)
            else:
                ans.append(arr[q-1])
            
        return ans