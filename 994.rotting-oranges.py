#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        
        minutes = 0
        while q and fresh:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = row + dr, col + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            minutes += 1

        return minutes if fresh == 0 else -1
        
# @lc code=end

