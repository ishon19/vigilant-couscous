from typing import List 

class DSU:
    def __init__(self, size):
        # Each node starts as it's own parent
        self.parent = list(range(size))
        # Rank helps to keep the tree balanced
        self.rank = [0] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # Union by rank, we attach smaller rank tree under root of higher rank tree
        px, py = self.find(x), self.find(y)

        # Cycle detected
        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # case 1: edges must be n-1
        if len(edges) != n-1:
            return False
        
        dsu = DSU(n)
        
        # case 2: no cycles
        for x, y in edges:
            if not dsu.union(x, y):
                return False
        
        # case 3: Exactly one connected component
        root = dsu.find(0)

        for i in range(1, n):
            if dsu.find(i) != root:
                return False
        
        return True