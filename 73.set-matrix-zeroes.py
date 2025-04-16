#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)
        
        for row in zero_rows:
            matrix[row] = [0] * n
        
        for col in zero_cols:
            for row in range(m):
                matrix[row][col] = 0

# @lc code=end

