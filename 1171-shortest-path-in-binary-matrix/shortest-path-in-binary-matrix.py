from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        n = len(grid)
        q = deque([(0, 0, 1)])  # (row, col, distance)
        visited = set((0, 0))

        while q:
            r, c, dist = q.popleft()
            if (r, c) == (n - 1, n - 1):
                return dist
            
            for dr, dc in [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, dist + 1))

        return -1
