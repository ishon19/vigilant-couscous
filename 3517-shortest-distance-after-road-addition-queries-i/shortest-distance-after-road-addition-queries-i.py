class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = {i: [i+1] for i in range(n-1)}
        res = []
        
        def bfs():
            q = deque([0])
            dist = {0: 0}
            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if neighbor not in dist:
                        dist[neighbor] = dist[node] + 1
                        if neighbor in graph:
                            q.append(neighbor)            
            return dist[n-1]

        for u, v in queries:
            graph[u].append(v)
            res.append(bfs())

        return res
