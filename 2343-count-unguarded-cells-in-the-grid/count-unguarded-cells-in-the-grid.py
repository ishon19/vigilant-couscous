class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['U'] * n for _ in range(m)]
        for r, c in guards:
            grid[r][c] = 'G'
        for r, c in walls:
            grid[r][c] = 'W'
        
        def mark_direction(r, c, dr, dc):
            while 0 <= r < m and 0 <= c < n:
                if grid[r][c] == 'G' or grid[r][c] == 'W':
                    break
                # mark the ones not safe anymore
                if grid[r][c] == 'U':
                    grid[r][c] = 'X'
                r += dr
                c += dc
        
        # traverse from all the guards
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r, c in guards:
            for dr, dc in dirs:
                mark_direction(r+dr, c+dc, dr, dc)
        
        unguarded_cells = sum(1 for r in range(m) for c in range(n) if grid[r][c] == 'U')
        return unguarded_cells