class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        q = deque([(0, 0, [(0,0)])])  # (row, col, path)
        seen = {(0, 0)}
        
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]
        
        while q:
            row, col, path = q.popleft()
            
            if row == rows - 1 and col == cols - 1:
                return len(path)
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and grid[nr][nc] == 0:
                    seen.add((nr, nc))
                    q.append((nr, nc, path + [(nr, nc)]))
        
        return -1