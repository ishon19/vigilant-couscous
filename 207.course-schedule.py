#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def findIndegrees(self, graph, numCourses):
        indegree = {i: 0 for i in range(numCourses)}
        
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        
        return indegree
    
    def topologicalSort(self, graph, numCourses):
        res = []
        q = deque()
        indegrees = self.findIndegrees(graph, numCourses)

        for node, indegree in indegrees.items():
            if indegree == 0:
                q.append(node)
        
        while q:
            node = q.popleft()
            res.append(node)

            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
        
        return res

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)
        
        order = self.topologicalSort(graph, numCourses)
        
        return len(order) == numCourses

# @lc code=end

