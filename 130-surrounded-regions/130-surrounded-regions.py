class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(r,c):
            # bounds check
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c]!='O':
                return 
            
            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        
        # flag the unsurrounded regions
        for r in range(rows):
            for c in range(cols):
                # if O and in the boundary
                if board[r][c] == 'O' and (r in [0, rows-1] or c in [0, cols-1]):
                    dfs(r,c)
        
        # capture the surrounded regions
        # which are those if they are still O even after 
        # initial flagging
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c] = 'X'
        
        # unset all the flagged regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='T':
                    board[r][c]='O'