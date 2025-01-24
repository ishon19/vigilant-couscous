#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def findIndegrees(self, graph, numCourses):
        indegrees = {i:0 for i in range(numCourses)}
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1        
        return indegrees
    
    def topologicalSort(self, graph, numCourses):
        res = []
        indegreeMap = self.findIndegrees(graph, numCourses)
        q = deque()        
        for node, indegree in indegreeMap.items():
            if indegree == 0:
                q.append(node)        
        while q:
            node = q.popleft()
            res.append(node)
            for neighbor in graph[node]:
                indegreeMap[neighbor] -= 1
                if indegreeMap[neighbor] == 0:
                    q.append(neighbor)
        return res

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # the idea is to do a topological sort on the pre-requisites and see if we can finish
        if not numCourses:
            return False
        
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        order = self.topologicalSort(graph, numCourses)
        return len(order) == numCourses
        


# @lc code=end

