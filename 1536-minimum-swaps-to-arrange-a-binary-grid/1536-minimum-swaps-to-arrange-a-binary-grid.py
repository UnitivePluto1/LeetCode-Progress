class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        zeroes = []
        n = len(grid)

        for row in grid:
            count = 0
            for j in range(n-1,-1,-1):
                if row[j] == 0:
                    count+=1
                else:
                    break
            zeroes.append(count)
        swaps=0
        for i in range(n):
            needed = n-i-1
            j=i
            while j<n and zeroes[j] < needed:
                j+=1
            if j==n:
                return -1
            while j>i:
                zeroes[j], zeroes[j-1] = zeroes[j-1],zeroes[j]
                j-=1
                swaps+=1
        return swaps
