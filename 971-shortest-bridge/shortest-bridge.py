class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        rows, cols = len(grid), len(grid[0])
        q = deque()

        # just so we mark ONE island as 2
        def find_first_land():
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        return i, j
        
        # mark island as 2
        def dfs(row, col):
            if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                grid[row][col] = 2
                q.append((row,col,0))
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    dfs(nr, nc)
        
        def bfs():
            while q:
                i, j, dist = q.popleft()
                
                for dr, dc in dirs:
                    nr, nc = i + dr, j + dc
                    if nr in range(rows) and nc in range(cols):
                        if grid[nr][nc] == 1:
                            return dist
                        elif grid[nr][nc] == 0:
                            grid[nr][nc] = -1
                            q.append((nr, nc, dist + 1))
                
            return -1
        
        start_row, start_col = find_first_land()
        dfs(start_row, start_col)

        return bfs()




