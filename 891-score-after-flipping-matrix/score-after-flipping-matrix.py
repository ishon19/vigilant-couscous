# class Solution:
#     def sumBin(self, grid):
#         res = 0
#         vals = []
#         for i in range(len(grid)):
#             vals.append(''.join([str(g) for g in grid[i]]))
        
#         for val in vals:
#             res += int(val, 2)
        
#         return res

#     def matrixScore(self, grid: List[List[int]]) -> int:
#         # by flipping the actual matrix
#         rows, cols = len(grid), len(grid[0])
        
#         # flip the rows first
#         # rows should start with zero for max effect
#         for r in range(rows):
#             for c in range(cols):
#                 if c == 0 and grid[r][c]==0:
#                     for i in range(1, cols):
#                         grid[r][i] = 1 - grid[r][i]
#                     # break
        
#         # for cols count and see if zeros are more, in which case we need to flip
#         for c in range(1, cols):
#             for r in range(rows):
#                 vals = collections.Counter([grid[c][i] for i in range(r)])
#                 if vals[0] > vals[1]:
#                     # flip the col
#                     for i in range(r):
#                         grid[i][c] = 1 - grid[i][c]
#                 # break
            
#         return self.sumBin(grid)
        

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Set score to summation of first column
        score = (1 << (n - 1)) * m

        # Loop over all other columns
        for j in range(1, n):
            count_same_bits = 0
            for i in range(m):
                # Count elements matching first in row
                if grid[i][j] == grid[i][0]:
                    count_same_bits += 1

            # Calculate score based on the number of same bits in a column
            count_same_bits = max(count_same_bits, m - count_same_bits)
            # Calculate the score contribution for the current column
            column_score = (1 << (n - j - 1)) * count_same_bits
            # Add contribution to score
            score += column_score

        return score