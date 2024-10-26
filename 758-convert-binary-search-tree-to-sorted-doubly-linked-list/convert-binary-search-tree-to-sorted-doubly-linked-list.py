"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # base case
        if not root:
            return None
            
        # Nodes to hold the information about the first and the last nodes
        first, last = None, None

        def in_order_traversal(node):
            nonlocal first, last 
            if not node:
                return 

            in_order_traversal(node.left)

            # process the current node
            if last:
                last.right = node
                node.left = last
            else:
                first = node
            
            # update last node
            last = node
            
            in_order_traversal(node.right)
        
        in_order_traversal(root)

        # close list
        last.right = first
        first.left = last

        return first