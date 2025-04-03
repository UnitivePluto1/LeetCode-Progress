class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        left, right = 0, r*c-1
        if target < matrix[0][0] or target > matrix[r-1][c-1]:
            return False
        while left <= right:
            mid = left+(right-left) // 2
            row = mid // c
            col = mid % c
            value = matrix[row][col]
            if value == target:
                return True
            elif value<target:
                left = mid+1
            else:
                right = mid-1
        return False