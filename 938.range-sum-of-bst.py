#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        self.res = 0
        
        def dfs(node):
            if node:
                self.res += node.val if node.val in range(low, high+1) else 0
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return self.res
                

# @lc code=end

