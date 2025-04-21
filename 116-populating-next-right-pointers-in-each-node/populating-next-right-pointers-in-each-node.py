"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = collections.deque([root])
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    l, r = node.left, node.right                
                    if l and r:
                        l.next = r
                    if l:
                        q.append(l)
                        level.append(l)
                    if r:
                        q.append(r)
                        level.append(r)

            for i in range(len(level)-1):
                level[i].next = level[i+1] or None
            
        return root
            
                
