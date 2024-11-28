class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # rows, cols = len(grid), len(grid[0])
        # obs_count = inf
        # dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        # q = deque([(0,0,0)])
        # visited = set()
        # while q:
        #     r, c, o = q.popleft()
        #     visited.add((r,c))
        #     if (r,c) == (rows-1, cols-1):
        #         obs_count = min(obs_count, o)
        #     for dr, dc in dirs:
        #         nr, nc = r + dr, c + dc
        #         if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited:
        #             if grid[nr][nc] == 1:
        #                 q.append((nr, nc, o + 1))
        #             else:
        #                 q.append((nr, nc, o))        
        # return obs_count
        
        """
        Typical BFS or even usual Dijkstra is not gonna cut it, we need a variant of it 0-1 BFS
        which uses deque instead of heap as we do in Dijkstras
        """
        rows, cols = len(grid), len(grid[0])
        dist = [[inf] * cols for _ in range(rows)]
        dist[0][0] = 0
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        q = deque([(0,0,0)])

        while q:
            o, r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0<=nr<rows and 0<=nc<cols and dist[nr][nc] == inf:                    
                    if grid[nr][nc] == 1:
                        dist[nr][nc] = o + 1
                        q.append((o+1, nr, nc))
                    else:
                        dist[nr][nc] = o
                        q.appendleft((o, nr, nc)) 
        return dist[rows-1][cols-1]





