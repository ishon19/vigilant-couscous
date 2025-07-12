class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
        
        q = deque([(0, 0, 1)])
        dirs = [(1,0),(0,1),(1,1),(-1,0),(0,-1),(1,-1),(-1,1),(-1,-1)]
        seen = set([(0,0)])

        while q:
            row, col, distance = q.popleft()

            if row == rows-1 and col == cols-1:
                return distance
            
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 0 and (nr, nc) not in seen:
                    q.append((nr, nc, distance + 1))
                    seen.add((nr, nc))

        return -1

