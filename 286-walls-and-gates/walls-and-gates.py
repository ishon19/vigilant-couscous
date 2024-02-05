class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # rows, cols = len(rooms), len(rooms[0])
        # visited = set()
        # q = collections.deque()

        # def addRoom(r,c):
        #     # boundary and wall check
        #     if r<0 or r>=rows or c<0 or c>=cols or rooms[r][c] == -1 or (r,c) in visited:
        #         return 
        #     visited.add((r,c))
        #     q.append((r,c))


        # for r in range(rows):
        #     for c in range(cols):
        #         # find all the gates and add to queue
        #         if rooms[r][c] == 0:
        #             q.append((r,c))
        #             visited.add((r,c))
        
        # dist = 0
        # while q:
        #     # pop elements from the queue
        #     for i in range(len(q)):
        #         r, c = q.popleft()
        #         rooms[r][c] = dist
        #         # now we can add the distance on the neighbors
        #         addRoom(r+1,c)
        #         addRoom(r, c+1)
        #         addRoom(r-1,c)
        #         addRoom(r, c-1)
        #     dist += 1
        if not rooms:
            return

        rows, cols = len(rooms), len(rooms[0])
        q =  collections.deque()

        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    q.append((row, col))
        
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                print(dr, dc)
                nr = r + dr
                nc = c + dc
                if nr in range(rows) and nc in range(cols) and rooms[nr][nc] == 2**31 - 1:
                    print('updating', rooms[nr][nc])
                    rooms[nr][nc] = 1 + rooms[r][c]
                    q.append((nr, nc))


                