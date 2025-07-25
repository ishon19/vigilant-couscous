class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n

        for i in range(n):
            if colors[i] != 0:
                continue

            q = deque([i])
            colors[i] = 1

            while q:
                node = q.popleft()

                for neighbor in graph[node]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[node]
                        q.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False 
        return True