class Solution:
    # TLE
    # def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    #     graph = collections.defaultdict(list)
    #     res = []

    #     for u, v in edges:
    #         graph[u].append(v)
    #         graph[v].append(u)

    #     heightMap = {}
    #     for i in range(n):
    #         q = collections.deque([i])
    #         seen = set()
    #         height = 0

    #         while q:
    #             for _ in range(len(q)):
    #                 node = q.popleft()
    #                 seen.add(node)

    #                 for nei in graph[node]:
    #                     if nei not in seen:
    #                         q.append(nei)
    #                         seen.add(nei)
    #             height += 1
    #         heightMap[i] = height

    #     mh = min(heightMap.values())
    #     for k, v in heightMap.items():
    #         if v == mh:
    #             res.append(k)
    #     return res

    def findMinHeightTrees(self, n, edges):
        if n<=2: return range(n)
        
        graph = collections.defaultdict(list)
        res = []

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        leaves = [k for k, v in graph.items() if len(v) == 1]

        # trim leaves till just 2 left
        while n > 2:
            n -= len(leaves)
            temp_leaves = []
            for i in leaves:
                # remove this leaf throughout
                leaf = graph[i].pop()
                graph[leaf].remove(i)
                if len(graph[leaf]) == 1:
                    temp_leaves.append(leaf)
            leaves = temp_leaves
        
        return leaves

        return res