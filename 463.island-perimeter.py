#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                
                # check left 
                if c-1 >= 0 and grid[r][c-1] == 1:
                    perimeter -= 2
                
                # check down 
                if r+1 < rows and grid[r+1][c] == 1:
                    perimeter -= 2

        return perimeter
# @lc code=end

