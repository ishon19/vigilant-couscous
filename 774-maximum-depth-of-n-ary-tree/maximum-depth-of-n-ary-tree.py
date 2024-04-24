"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
            
        res = 0
        q = collections.deque([root])
        seen = set()

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                seen.add(node)

                for neighbor in node.children:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        q.append(neighbor)
            res += 1
        
        return res