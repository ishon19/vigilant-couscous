#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#

# @lc code=start
class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # since this is a closest distance problem, we would do a 
        # bfs based traversal.
        rows, cols = len(grid), len(grid[0])
        q = deque()
        seen = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))
        
        while q:
            row, col = q.popleft()
            seen.add((row, col))
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = row + dr, col + dc
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 2**31 - 1 and (nr, nc) not in seen:
                    grid[nr][nc] = 1 + grid[row][col] 
                    q.append((nr, nc))
# @lc code=end

