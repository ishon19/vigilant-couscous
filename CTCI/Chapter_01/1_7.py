"""
CTCI 1.7: Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a
method to rotate the image by 90 degrees. Can you do this in place?

Example:
Input:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
 
Output:
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
"""

def rotate_matrix(matrix):
    """
    Time: O(N^2)
    Space: O(1)
    """
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        
        for i in range(first, last):
            offset = i - first
            
            # Save top
            top = matrix[first][i]
            
            # Left -> Top
            matrix[first][i] = matrix[last - offset][first]
            
            # Bottom -> Left
            matrix[last - offset][first] = matrix[last][last - offset]
            
            # Right -> Bottom
            matrix[last][last - offset] = matrix[i][last]
            
            # Top -> Right
            matrix[i][last] = top
            
    return matrix