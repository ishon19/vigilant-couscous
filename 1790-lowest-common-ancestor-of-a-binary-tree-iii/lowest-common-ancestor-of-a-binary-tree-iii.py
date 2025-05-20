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
        # ptr1 = p
        # ptr2 = q

        # while ptr1 != ptr2:
        #     ptr1 = ptr1.parent if ptr1.parent else q
        #     ptr2 = ptr2.parent if ptr2.parent else p
        
        # return ptr1
        def get_depth(node):
            depth = 0
            while node.parent:
                depth += 1
                node = node.parent
            return depth 
        
        p_depth = get_depth(p) 
        q_depth = get_depth(q)

        while p_depth > q_depth:
            p = p.parent
            p_depth -= 1
        
        while q_depth > p_depth:
            q = q.parent
            q_depth -= 1
        
        while p != q:
            p = p.parent
            q = q.parent 
        
        return p