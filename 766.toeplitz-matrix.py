#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows - 1):
            for j in range(cols - 1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        
        return True
        
# @lc code=end

