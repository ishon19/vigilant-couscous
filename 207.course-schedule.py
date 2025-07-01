#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses:
            return False 

        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        indegree = {i:0 for i in range(numCourses)}
        for prereq, courses in graph.items():
            for course in courses:
                indegree[course] += 1
        
        q = deque([course for course in indegree.keys() if indegree[course] == 0])
        order = []

        while q:
            node = q.popleft()
            order.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return len(order) == numCourses

# @lc code=end

