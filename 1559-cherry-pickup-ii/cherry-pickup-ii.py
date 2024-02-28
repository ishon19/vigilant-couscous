import functools

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        @functools.cache
        def dp(row, col1, col2):
            if col1 in range(cols) and col2 in range(cols):
                res = 0
                res += grid[row][col1]
                if col1 != col2:
                    res += grid[row][col2]
                
                if row != rows - 1:
                    res += max(dp(row+1, new_col1, new_col2)
                              for new_col1 in [col1, col1+1, col1-1]
                              for new_col2 in [col2, col2+1, col2-1])
                
                return res
            return float("-inf")
        
        return dp(0, 0, cols-1)