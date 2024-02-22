class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n <= 1:
            return 1
        
        if not trust:
            return -1
            
        graph = collections.defaultdict(list)
        indegree = {node: 0 for relation in trust for node in relation}
        outdegree = {node: 0 for relation in trust for node in relation}

        for i, j in trust:
            graph[i].append(j)
            indegree[j] += 1
            outdegree[i] += 1
        
        # print(indegree, outdegree, graph)
        for k, v in indegree.items():
            if v == n - 1 and outdegree[k] == 0:
                return k

        return -1