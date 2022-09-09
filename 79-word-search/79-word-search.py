class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        path = set()
        
        def helper(i,r,c):
            if i == len(word):
                return True
            if min(r,c)<0 or r>=rows or c>=cols or (r,c) in path or word[i] != board[r][c]:
                return False
            path.add((r,c))                                    
            res =  (helper(i+1, r+1,c) or helper(i+1, r, c+1) or helper(i+1, r-1, c) or helper(i+1, r, c-1))
            path.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if helper(0,r,c): return True
        return False
            
            