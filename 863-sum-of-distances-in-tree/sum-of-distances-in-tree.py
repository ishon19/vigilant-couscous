class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        """
         Two dfs approach
         Calculate the sum of nodes on each subtree
        """
        counts = [1] * n
        res = [0] * n

        def dfs1(node, parent):
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                dfs1(neighbor, node)
                counts[node] += counts[neighbor]
                res[node] += res[neighbor] + counts[neighbor]
        
        def dfs2(node, parent):
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue                
                res[neighbor] = res[node] - counts[neighbor] + (n - counts[neighbor])
                dfs2(neighbor, node)
        
        dfs1(0,-1)
        dfs2(0,-1)
        
        return res