#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        res = []

        while left < right and top < bottom:
            # L -> R
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # T -> B
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
            
            # R -> L
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res
        
# @lc code=end

