class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.diameter = 0
    
    def dfs(self, node, parent):
        depth1 = 0
        depth2 = 0

        for child in self.graph[node]:
            if child != parent:
                depth = 1 + self.dfs(child, node)
                if depth > depth1:
                    depth1, depth2 = depth, depth1
                elif depth > depth2:
                    depth2 = depth
        self.diameter = max(self.diameter, depth1 + depth2)    
        return depth1

    def treeDiameter(self, edges: List[List[int]]) -> int:
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)        
        self.dfs(0, -1)
        return self.diameter