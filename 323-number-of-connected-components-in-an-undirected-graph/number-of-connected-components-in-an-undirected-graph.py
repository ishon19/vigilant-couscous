class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.components = size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[py] < self.rank[px]:
            self.parent[py] = px
        else:
            self.parent[px] = py
            self.rank[py] += 1
        
        self.components -= 1
        return True

    def areConnected(self, x, y):
        return self.find(x) == self.find(y) 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)
        return uf.components        