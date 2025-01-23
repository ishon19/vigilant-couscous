"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        def dfs(node):
            nonlocal diameter
            if not node or not node.children:
                return 0

            depth1 = 0
            depth2 = 0

            for child in node.children:
                depth = 1 + dfs(child)
                if depth > depth1:
                    depth1, depth2 = depth, depth1
                elif depth > depth2:
                    depth2 = depth
            diameter = max(diameter, depth1 + depth2)
            return depth1

        diameter = 0
        dfs(root)
        return diameter

