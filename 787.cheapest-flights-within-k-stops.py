#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        prices = [float("inf")] * n
        prices[src] = 0

        for price, to, frm in flights:
            graph[frm].append((to, price))
        
        heap = [(src, prices[src], 0)]
        heapify(heap)

        while heap:
            source, price, steps = heappop(heap)

            if price > prices[source] or steps > k:
                continue
            
            if source == dst:
                return price
            
            for neighbor in graph[source]:
                heappush(heap, (price, steps + 1))
        



# @lc code=end

