#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        coverageMap = defaultdict(int)
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        idx = 2

        def dfs(row, col, idx):
            if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                grid[row][col] = idx
                area = 1
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    area += dfs(nr, nc, idx)                
                return area
            return 0
        
        # label the islands and calculate the sizes 
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    coverageMap[idx] = dfs(row, col, idx)
                    idx += 1
        
        if not coverageMap:
            return 1
        
        res = max(coverageMap.values())

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    neighbors = set()
                    for dr, dc in dirs:
                        nr, nc = row + dr, col + dc
                        if nr in range(rows) and nc in range(cols) and grid[nr][nc] >= 2:
                            neighbors.add(grid[nr][nc])
                    
                    size = 1
                    for check_idx in neighbors:
                        size += coverageMap[check_idx]
                    
                    res = max(res, size)

        return res
# @lc code=end

