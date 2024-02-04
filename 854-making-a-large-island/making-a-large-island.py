class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(row, col, idx):
            if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                grid[row][col] = idx
                return 1 + dfs(row + 1, col, idx) + dfs(row - 1, col, idx) + dfs(row, col + 1, idx) + dfs(row, col - 1, idx)
            return 0

        idx = 2
        area = {}

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area[idx] = dfs(row, col, idx)
                    idx += 1

        res = max(area.values(), default=0)
        if res == 0:
            return 1 if rows * cols else 0

        # flip the zeros
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    nearby_points = {grid[i][j] for i, j in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)) if i in range(rows) and j in range(cols)}
                    nearby_points = {i for i in nearby_points if i != 0}
                    res = max(res, 1 + sum(area[i] for i in nearby_points))

        return res if res else rows * cols