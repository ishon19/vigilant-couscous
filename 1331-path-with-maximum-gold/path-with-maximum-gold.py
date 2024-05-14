class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = float("-inf")
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(r, c, pattern, visited):
            nonlocal res
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] > 0:
                visited.add((r, c))
                pattern.append(grid[r][c])
                res = max(res, sum(pattern))
                for dr, dc in dirs:
                    dfs(r + dr, c + dc, pattern, visited)
                pattern.pop()
                visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, [], set())

        return res if res != float("-inf") else 0
