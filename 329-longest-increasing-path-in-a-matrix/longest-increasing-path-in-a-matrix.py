class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # mem = {}
        # rows = len(matrix)
        # cols = len(matrix[0])

        # def dfs(r, c, prev):
        #     # check for bounds
        #     if r>=rows or r<0 or c>=cols or c<0 or matrix[r][c]<=prev:
        #         return 0
            
        #     if (r, c) in mem:
        #         return mem[(r,c)]
            
        #     streak = 1
        #     # perform dfs in all directions
        #     streak = max(streak, 1 + dfs(r, c+1, matrix[r][c]))
        #     streak = max(streak, 1 + dfs(r, c-1, matrix[r][c]))
        #     streak = max(streak, 1 + dfs(r+1, c, matrix[r][c]))
        #     streak = max(streak, 1 + dfs(r-1, c, matrix[r][c]))
        #     mem[(r,c)] = streak
        #     return streak
        
        # for r in range(rows):
        #     for c in range(cols):
        #         dfs(r,c,-1)
        
        # return max(mem.values())
        # topological sort based approach this problem
        # if we see it like each cell pointing to a value
        # larger than it
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        indegrees = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for dr, dc in dirs:
                    nr, nc = i + dr, j + dc
                    if nr in range(m) and nc in range(n) and matrix[nr][nc] > matrix[i][j]:
                        indegrees[nr][nc] += 1
        
        q = deque((i,j) for i in range(m) for j in range(n) if indegrees[i][j] == 0)
        pathLength = 0

        while q:
            pathLength += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for dr, dc in dirs:
                    nr, nc = i + dr, j + dc
                    if nr in range(m) and nc in range(n) and matrix[nr][nc] > matrix[i][j]:
                        indegrees[nr][nc] -= 1
                        if indegrees[nr][nc] == 0:
                            q.append((nr, nc))
        
        return pathLength