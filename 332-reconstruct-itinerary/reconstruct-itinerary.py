class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # construct the graph
        graph = collections.defaultdict(list)

        for src, dest in tickets:
            # we keep the order sorted using a heap
            heapq.heappush(graph[src], dest)
        
        itinerary = []

        def dfs(airport):
            # keeping popping from the heap
            # means visit all destinations from current airport
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)
            
            itinerary.append(airport)
        
        dfs("JFK")

        return itinerary[::-1]

