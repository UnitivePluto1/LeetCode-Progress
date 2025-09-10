class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = float('inf')
        maxP = 0

        for v in prices:
            if v < minP:
                minP = v
            elif v - minP > maxP:
                maxP = v-minP
        return maxP