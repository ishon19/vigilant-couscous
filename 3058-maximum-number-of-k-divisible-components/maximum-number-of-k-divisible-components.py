class Solution:          
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        components = 0
        
        def dfs(node: int, parent: int) -> int:
            nonlocal components
            
            subtree_sum = values[node]
        
            for neighbor in graph[node]:
                if neighbor != parent:
                    subtree_sum += dfs(neighbor, node)
            
            if subtree_sum % k == 0:
                components += 1
                return 0
                
            return subtree_sum
        
        dfs(0, -1)
        return components