"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

"""
This is like finding an intersection of the linked lists. The key information here
is the presence of the parent node.

The nodes can be at different depths so we need to move the one deeper
in the tree up until both pointer are at the same level.

Once they are at the same level, they can be simultaneously moved upwards
until they converge. 
"""
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def get_depth(node):
            depth = 0
            while node:
                node = node.parent
                depth += 1
            return depth
        
        # find the depth of both nodes
        depth_p = get_depth(p)
        depth_q = get_depth(q)

        # equalize the depth if they are different
        while depth_p > depth_q:
            p = p.parent
            depth_p -= 1
        
        while depth_q > depth_p:
            q = q.parent
            depth_q -= 1
        
        # move up till they both intersect
        while p != q:
            p = p.parent
            q = q.parent
        
        return q

