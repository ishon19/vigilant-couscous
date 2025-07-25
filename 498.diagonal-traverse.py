#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        res = []
        
        def helper(row, col, dir):
            curr = []
            while row < rows and col >= 0:
                curr.append(mat[row][col])
                row += 1 
                col -= 1
            return curr if dir == 1 else curr[::-1]
        
        direction = -1
        for col in range(cols):
            res.extend(helper(0, col, direction))
            direction = -direction
        
        for row in range(1, rows):
            res.extend(helper(row, cols-1, direction))
            direction = -direction
        
        return res
        
# @lc code=end

