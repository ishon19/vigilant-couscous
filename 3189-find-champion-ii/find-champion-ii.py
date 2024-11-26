class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
        
        indegrees = [0] * n

        for k, v in graph.items():
            for node in v:
                indegrees[node] += 1

        # count zeros
        zcount = 0
        last = -1
        for i, degree in enumerate(indegrees): 
            if degree == 0 and zcount > 1:
                return -1 
            elif degree == 0:
                zcount += 1
                last = i
            if i == len(indegrees) - 1 and zcount == 1:
                return last
        return -1