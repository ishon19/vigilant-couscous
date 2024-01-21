"""
CTCI 1.8: Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are
set to 0.

Example:
Input:
[[1, 2, 3],
 [4, 0, 6],
 [7, 8, 9]]
 
Output:

[[1, 0, 3],
[0, 0, 0],
[7, 0, 9]]
"""

def zero_matrix(matrix):
    """
    Time: O(N^2)
    Space: O(1)
    """
    m = len(matrix)
    n = len(matrix[0])
    rows = set()
    cols = set()
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
                
    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0
                
    return matrix