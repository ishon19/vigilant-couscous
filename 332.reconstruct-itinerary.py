#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dest in tickets:
            heappush(adj[src], dest)
        
        route = []
        def visit(airport):
            while adj[airport]:
                visit(heappop(adj[airport]))
            route.append(airport)
        
        visit('JFK')
        return route[::-1]
# @lc code=end

