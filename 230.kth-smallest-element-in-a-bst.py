#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            order.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return order[k-1]
# @lc code=end

