#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not root.left and not root.right:
            return True
        
        def dfs(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            return p.val == q.val and dfs(p.left, q.right) and dfs(p.right, q.left)
        
        return dfs(root.left, root.right)
# @lc code=end

