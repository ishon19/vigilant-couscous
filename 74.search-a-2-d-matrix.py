#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False 
        
        l, r = 0, len(matrix) * len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid//len(matrix)][mid%len(matrix[0])]

            if val == target:
                return True
            elif val > target:
                r = mid - 1
            else:
                l = mid + 1

        return False  
    
# @lc code=end

