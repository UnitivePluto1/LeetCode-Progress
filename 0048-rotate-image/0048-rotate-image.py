class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        
        r = len(matrix)
        c = len(matrix[0])

        # Transpose

        for i in range(r):
            for j in range(i, c):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse

        for i in range(r):
            for j in range(0, c//2):
                matrix[i][c - j - 1], matrix[i][j] =  matrix[i][j], matrix[i][c - j - 1]
        

        return matrix