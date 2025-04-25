class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, (rows * cols) - 1

        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid//cols][mid%cols]

            if val == target:
                return True
            elif val > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False