class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # the trick here is to flip a whole row and see if a matching row is found
        res = 0

        for row in matrix:
            flipped_row = [1-x for x in row]
            res = max(res, sum(1 if cur_row == row or cur_row == flipped_row else 0 for cur_row in matrix))

        return res