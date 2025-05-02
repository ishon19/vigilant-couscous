class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for from_node, to_node in edges:
            graph[to_node].append(from_node)
        
        seen = [None] * n

        def dfs(node):
            if seen[node]:
                return seen[node]
            
            ancestors = set()
            for ancestor in graph[node]:
                ancestors.add(ancestor)
                ancestors.update(dfs(ancestor))
            
            seen[node] = ancestors
            return ancestors
        
        results = []
        for i in range(n):
            results.append(sorted(list(dfs(i))))
        return results
            

