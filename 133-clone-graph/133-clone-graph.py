"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodeMap = {}
        
        def dfs(node):
            # if copy found, return
            if node in nodeMap:
                return nodeMap[node]
            
            # else create the copy
            copy = Node(node.val)
            nodeMap[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        
        return dfs(node) if node else None
            