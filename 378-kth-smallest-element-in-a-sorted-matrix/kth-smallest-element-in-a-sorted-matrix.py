class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        seen = set()
        n = len(matrix)

        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))
            seen.add((i, 0))
        
        for i in range(k-1):
            value, row, col = heapq.heappop(heap)

            if col + 1 < n and (row, col + 1) not in seen:
                heapq.heappush(heap, (matrix[row][col+1], row, col+ 1))
                seen.add((row, col + 1))
        
        return heapq.heappop(heap)[0]