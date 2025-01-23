class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []

        def improvement(p, t):
            return (((p+1)/(t+1)) - (p/t))

        for passing, total in classes:
            heapq.heappush(heap, (-improvement(passing, total), passing, total))
        
        while extraStudents:
            _, p, t = heapq.heappop(heap)
            heapq.heappush(heap, (-improvement(p+1, t+1), p+1, t+1))
            extraStudents -= 1
        
        res = 0
        n = len(heap)
        while heap:
            _, p, t = heapq.heappop(heap)
            res += p / t

        return res/n