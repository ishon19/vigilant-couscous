#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegrees = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[prereq] += 1
        
        q = deque([course for course in range(numCourses) if indegrees[course] == 0])
        
        while q:
            pass
            
        return 
            

# @lc code=end

