#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # once again start from the edges and move your way up 
        if not board or not board[0]:
            return 
        
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            if r in range(rows) and c in range(cols) and board[r][c] == 'O':
                board[r][c] = 'T'
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r + dr, c + dc
                    capture(nr, nc)
        
        # start from the edges
        for r in range(rows):
            capture(r, 0)
            capture(r, cols-1)
        
        for c in range(cols):
            capture(0, c)
            capture(rows-1, c)
        
        # cleanup
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
# @lc code=end

