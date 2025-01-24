#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import defaultdict, deque
from typing import List

class Solution:
    def __init__(self):
        self.numCourses = 0
        self.preRequisites = []
        self.graph = {}
    
    def __constructGraph(self):
        graph = defaultdict(list)
        for course, prereq in self.preRequisites:
            graph[prereq].append(course)        
        self.graph = graph
    
    def __findIndegrees(self):
        indegrees = {i:0 for i in range(self.numCourses)}
        for node in self.graph:
            for neighbor in self.graph[node]:
                indegrees[neighbor] += 1        
        return indegrees

    def __topologicalSort(self):
        indegrees = self.__findIndegrees()
        order = []
        q = deque()

        # initialize the queue
        for node, indegree in indegrees.items():
            if indegree == 0:
                q.append(node)
        
        # find all dependencies with 0 indegrees
        while q:
            node = q.popleft()
            order.append(node)
            for neighbor in self.graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)        
        return order 

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.numCourses = numCourses
        self.preRequisites = prerequisites

        self.__constructGraph()
        order = self.__topologicalSort()

        return order if len(order) == numCourses else []
        
# @lc code=end

