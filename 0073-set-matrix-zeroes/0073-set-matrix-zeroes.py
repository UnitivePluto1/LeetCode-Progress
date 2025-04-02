class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowlen = len(matrix)
        collen = len(matrix[0])
        ro = set()
        col = set()
        for i in range(rowlen):
            for k in range(collen):
                if matrix[i][k] == 0:
                    ro.add(i)
                    col.add(k)
        def rowZero(row):
            for column in range(collen):
                matrix[row][column] = 0
        def colZero(col):
            for row in range(rowlen):
                matrix[row][col] = 0
        for i in ro:
            rowZero(i)
        for i in col:
            colZero(i)
                
