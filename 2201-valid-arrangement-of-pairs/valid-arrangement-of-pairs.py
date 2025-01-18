class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        order = defaultdict(int)

        for x, y in pairs:
            graph[x].append(y)
            order[x] += 1
            order[y] -= 1
            src = x
        
        for key in order:
            if order[key] == 1:
                src = key
                break

        res = []
        def dfs(node):
            while graph[node]:
                new_node = graph[node].pop()
                dfs(new_node)
            res.append(node)
        dfs(src)
        return list(pairwise(res[::-1]))