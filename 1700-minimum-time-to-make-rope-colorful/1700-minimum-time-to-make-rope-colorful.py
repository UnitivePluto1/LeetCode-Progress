class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        i = j = 0
        n = len(neededTime)
        while i<n and j<n:
            currT = 0
            currM = 0
            while j<n and colors[i] == colors[j]:
                currT += neededTime[j]
                currM = max(currM, neededTime[j])
                j+=1
            total += currT - currM
            i=j

        return total            