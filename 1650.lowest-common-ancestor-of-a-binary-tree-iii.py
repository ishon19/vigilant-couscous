#
# @lc app=leetcode id=1650 lang=python3
#
# [1650] Lowest Common Ancestor of a Binary Tree III
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        node1, node2 = p, q
        
        while node1 != node2:
            node1 = node1.parent if node1.parent else q
            node2 = node2.parent if node2.parent else p
        
        return node1
            

# @lc code=end

