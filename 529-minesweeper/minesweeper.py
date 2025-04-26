class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return []
        
        rows, cols = len(board), len(board[0])
        row, col = click

        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        
        directions = [(1,0),(-1,0),(1,1),(-1,-1),(0,1),(0,-1),(1,-1),(-1,1)]

        def dfs(x, y):
            if x in range(rows) and y in range(cols) and board[x][y] == 'E':
                mines = 0
                for dr, dc in directions:
                    nr, nc = x + dr, y + dc
                    if nr in range(rows) and nc in range(cols) and board[nr][nc] in ['X', 'M']:
                        mines += 1
                
                if mines:
                    board[x][y] = str(mines)
                else:
                    board[x][y] = 'B'
                    for dr, dc in directions:
                        dfs(x + dr, y + dc)
        
        dfs(row, col)
        return board