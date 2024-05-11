class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratioed = sorted([(w/q, w, q) for w, q in zip(wage, quality)])
        heap = []
        current_quality = 0
        res = float("inf")

        for r, w, q in ratioed:
            heapq.heappush(heap, -q)
            current_quality += q
            if len(heap) > k: current_quality += heapq.heappop(heap)
            if len(heap) == k: res = min(res, r * current_quality)
        
        return res
