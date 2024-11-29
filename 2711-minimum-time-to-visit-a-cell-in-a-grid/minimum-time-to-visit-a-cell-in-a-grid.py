class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1 
            
        rows, cols = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        pq = [(grid[0][0],0,0)]
        seen = set()

        while pq:
            t,r,c = heapq.heappop(pq)

            if (r,c) == (rows-1, cols-1):
                return t
            
            if (r,c) in seen:
                continue
            seen.add((r,c))
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0<=nr<rows and 0<=nc<cols and (nr, nc) not in seen:
                    wait = 1 if (grid[nr][nc] - t) % 2 == 0 else 0
                    next_time = max(grid[nr][nc] + wait, t + 1)
                    heapq.heappush(pq, (next_time,nr,nc))
        return -1