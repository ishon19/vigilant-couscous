class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if r in range(rows) and c in range(cols) and (r, c) not in visited and grid[r][c] != 0:
                visited.add((r, c))
                return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c+1) + dfs(r, c-1)
            return 0
        
        res = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    res = max(res, dfs(row, col))
        
        return res