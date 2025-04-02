class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        
        maxP = 0 

        while j<len(prices):
            curr = prices[j] - prices[i]
            if prices[i]<=prices[j]:
                maxP = max(curr,maxP) 
            elif prices[j]<prices[i]:
                i=j
            j += 1
        return maxP
            