#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=-inf, high=inf) -> bool:
        if not root:
            return True
        
        if not low < root.val < high:
            return False
        
        return self.isValidBST(root.left, low, root.val) and self.isValidBST(root.right, root.val, high)
        
# @lc code=end

