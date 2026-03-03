class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        mini = float('inf')
        ans = []
        arr.sort()

        for i in range(1,len(arr)):
            curr = abs(arr[i] - arr[i-1])
            if curr<mini:
                mini=curr
                ans=[[arr[i-1],arr[i]]]
            elif curr == mini:
                ans.append([arr[i-1],arr[i]])

        return ans