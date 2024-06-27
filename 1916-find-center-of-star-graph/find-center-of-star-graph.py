class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        for k, v in graph.items():
            if len(v) == len(edges):
                return k
        
        return -1 