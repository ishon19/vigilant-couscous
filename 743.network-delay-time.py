#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # this is a classic dijkstra's problem 
        # create the graph first 
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        # init distances 
        dist = {i:float("inf") for i in range(1, n + 1)}
        dist[k] = 0

        pq = [(0, k)] # (time, node)

        while pq:
            d, node = heappop(pq)
            if d > dist[node]:
                continue

            for neighbor, time in adj[node]:
                newDist = d + time
                if newDist < dist[neighbor]:
                    dist[neighbor] = newDist
                    heappush(pq, (newDist, neighbor))
        
        maxTime = max(dist.values())
        return maxTime if maxTime < float("inf") else -1

# @lc code=end

