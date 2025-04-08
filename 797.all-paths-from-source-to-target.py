#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def dfs(node, path):
            path.append(node)

            if node == len(graph) - 1:
                res.append(path[:])
            else:
                for neighbor in graph[node]:
                    dfs(neighbor, path)
            
            path.pop()
        
        dfs(0, [])
        return res
# @lc code=end

