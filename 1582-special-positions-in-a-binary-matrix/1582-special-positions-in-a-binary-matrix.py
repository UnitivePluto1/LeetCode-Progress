class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        row = [0] * n
        col = [0] * m
        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and row[i] == 1 and col[j] == 1:
                    ans+=1

        return ans