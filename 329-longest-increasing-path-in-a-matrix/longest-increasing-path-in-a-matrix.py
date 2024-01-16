class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        mem = {}
        rows = len(matrix)
        cols = len(matrix[0])

        def dfs(r, c, prev):
            # check for bounds
            if r>=rows or r<0 or c>=cols or c<0 or matrix[r][c]<=prev:
                return 0
            
            if (r, c) in mem:
                return mem[(r,c)]
            
            streak = 1
            # perform dfs in all directions
            streak = max(streak, 1 + dfs(r, c+1, matrix[r][c]))
            streak = max(streak, 1 + dfs(r, c-1, matrix[r][c]))
            streak = max(streak, 1 + dfs(r+1, c, matrix[r][c]))
            streak = max(streak, 1 + dfs(r-1, c, matrix[r][c]))
            mem[(r,c)] = streak
            return streak
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,-1)
        
        return max(mem.values())