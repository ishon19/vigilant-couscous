class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # preMap = {i:[] for i in range(numCourses)}

        # for c, p in prerequisites:
        #     preMap[c].append(p)
        
        # res = []
        # visited, cycle = set(), set()
        
        # # perform the topological sorting
        # def dfs(course):
        #     if course in cycle:
        #         return False
        #     if course in visited:
        #         return True
            
        #     cycle.add(course)
        #     for c in preMap[course]:
        #         if not dfs(c): return False
            
        #     cycle.remove(course)
        #     visited.add(course)
        #     res.append(course)
        #     return True
        
        # for c in range(numCourses):
        #     if not dfs(c):
        #         return []
        # return res
        graph = defaultdict(list)
        res = []
        indegree = {}

        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            indegree[pair[0]] = indegree.get(pair[0], 0) + 1

        q = deque([])
        for i in range(numCourses):
            if(i not in indegree):
                q.append(i)

        order = []
        while q:
            cur = q.popleft()
            order.append(cur)

            if(cur in graph):
                for n in graph[cur]:
                    indegree[n] -= 1
                    if(indegree[n] == 0):
                        q.append(n)

        return order if(len(order) == numCourses) else []
