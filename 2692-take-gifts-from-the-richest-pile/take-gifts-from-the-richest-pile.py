class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:        
        heap = []

        for i in range(len(gifts)):
            heapq.heappush(heap, -gifts[i])

        while k:
            top = -heapq.heappop(heap)
            top = floor(sqrt(top))
            heapq.heappush(heap, -top)
            k -= 1
        
        return -sum(heap)