#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        n = len(grid)
        dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]

        q = deque([(0,0,1)])

        while q:
            row, col, dist = q.popleft()
            grid[row][col] = 1

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc

                if nr == n - 1 and nc == n - 1 and grid[nr][nc] != 1:
                    return dist + 1

                if nr in range(n) and nc in range(n) and grid[nr][nc] == 0:
                    q.append((nr, nc, dist + 1))
        
        return -1


# @lc code=end

