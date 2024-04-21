class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = collections.defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)   

        if destination in graph[source]:
            return True         

        q = collections.deque([source])
        seen = set([source])

        while q:
            root = q.popleft()
            seen.add(root)

            if root == destination:
                return True

            for node in graph[root]:
                if node not in seen:
                    if node == destination:
                        return True 
                    seen.add(node)       
                    q.append(node)
        
        return False

