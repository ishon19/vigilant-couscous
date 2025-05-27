class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        rows, cols = len(nums), len(nums[0])
        res = []

        q = deque([(0, 0)])
        seen = set((0, 0))

        while q:
            row, col = q.popleft()
            res.append(nums[row][col])

            if row + 1 < rows and col < len(nums[row+1]) and (row+1, col) not in seen:
                seen.add((row+1, col))
                q.append((row+1, col))
            
            if col + 1 < len(nums[row]) and row < rows and (row, col+1) not in seen:
                seen.add((row, col+1))
                q.append((row, col+1))
        
        return res