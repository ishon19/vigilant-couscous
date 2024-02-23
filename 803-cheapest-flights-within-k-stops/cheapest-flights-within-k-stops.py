class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for frm, to, price in flights:
            graph[frm].append((price, to))
        
        # cost, source, cur_stops
        heap = [(0, src, 0)]

        visited = {}

        while heap:
            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost
            
            # check if the node is visited and had same or lower cost move forward
            if (node, stops) in visited and visited[(node, stops)] <= cost:
                continue
                
            visited[(node, stops)] = cost

            if stops <= k:
                for price, to in graph[node]:
                    heapq.heappush(heap, (price + cost, to, stops + 1))

        return -1