import heapq
import collections

class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = collections.defaultdict(list)

        # Building the graph
        for frm, to, cost in highways:
            graph[frm].append((cost, to))
            graph[to].append((cost, frm))
        
        heap = [(0, 0, 0)] # Cost, node, discounts used
        visited = {} # key: (node, discount used), value: cost

        while heap:
            cost, node, discount_used = heapq.heappop(heap)
            
            # If this node with the current discount usage has been visited with a cheaper cost, continue
            if (node, discount_used) in visited and visited[(node, discount_used)] <= cost:
                continue

            # If the destination is reached, return the cost
            if node == n - 1:
                return cost
            
            visited[(node, discount_used)] = cost
            
            for c, neighbor in graph[node]:
                # If discounts are available, consider the path with and without using a discount
                if discount_used < discounts:
                    # Consider the next edge with the discount
                    heapq.heappush(heap, (cost + c // 2, neighbor, discount_used + 1))
                # Always consider the path without using a discount (if no discounts left or to save for later)
                heapq.heappush(heap, (cost + c, neighbor, discount_used))
        
        return -1
