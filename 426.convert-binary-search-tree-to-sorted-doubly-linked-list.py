#
# @lc app=leetcode id=426 lang=python3
#
# [426] Convert Binary Search Tree to Sorted Doubly Linked List
#

# @lc code=start
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
        # Pre order traversal to keep it sorted 
        if not root:
            return None

        self.first = None
        self.last = None

        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)

            # connect current node with the previous one
            if self.last:
                self.last.right = node
                node.left = self.last
            else:
                self.first = node
            
            self.last = node

            inorder(node.right)
        
        inorder(root)

        # make it circular
        self.last.right = self.first
        self.first.left = self.last

        return self.first

# @lc code=end

