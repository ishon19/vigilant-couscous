class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows, cols = len(maze), len(maze[0])

        start, destination = tuple(start), tuple(destination)
        q = deque([start])
        seen = set([start])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            curr_row, curr_col = q.popleft()

            # check if we have reached the destination
            if (curr_row, curr_col) == destination:
                return True
            
            for dr, dc in dirs:
                nr, nc = curr_row, curr_col

                # roll until we hit the wall 
                while nr+dr in range(rows) and nc+dc in range(cols) and maze[nr+dr][nc+dc] == 0:
                    nr += dr
                    nc += dc
                
                if (nr, nc) not in seen:
                    seen.add((nr, nc))
                    q.append((nr, nc))
        
        return False
