class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        thieves = [(r,c) for r in range(rows) for c in range(cols) if grid[r][c] == 1]
        dirs = [(0,1),(-1,0),(0,-1),(1,0)]

        # precompute the distance of each from from each thief
        def compute_distances():
            distances = [[float("inf")] * cols for _ in range(rows)]
            q = collections.deque(thieves)
            for r, c in thieves:
                distances[r][c] = 0            
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0<=nr<rows and 0<=nc<cols and distances[nr][nc] == float("inf"):
                        distances[nr][nc] = 1 + distances[r][c]
                        q.append((nr, nc))            
            return distances
        
        distances = compute_distances()
        pq = [(-distances[0][0], 0, 0)]  # (negative safeness, row, col)
        visited = set()
        
        while pq:
            safeness, r, c = heappop(pq)
            safeness = -safeness
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == rows - 1 and c == cols - 1:
                return safeness
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    heappush(pq, (-min(safeness, distances[nr][nc]), nr, nc))

        return 0