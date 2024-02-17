class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # min heap version
        ladders_alloc = []

        for i in range(len(heights) - 1):
            climb = heights[i+1] - heights[i]

            if climb <= 0:
                continue
            
            heapq.heappush(ladders_alloc, climb)
            
            # use ladder
            if len(ladders_alloc) <= ladders:
                continue
            
            bricks -= heapq.heappop(ladders_alloc)

            if bricks < 0:
                return i
        
        return len(heights) - 1