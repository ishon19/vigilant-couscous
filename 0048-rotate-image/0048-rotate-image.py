class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = []
        for col in range(len(matrix[0])):
            arr = []
            for row in range(len(matrix)):
                arr.append(matrix[row][col])
            temp.append(arr[::-1])
        print(temp)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = temp[i][j]