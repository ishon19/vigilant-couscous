class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        res = 0
        heights = [0] * (n + 1)

        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            stack = []

            for i in range(n + 1):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] -1
                    res = max(res, h * w)
                stack.append(i)
        
        return res
