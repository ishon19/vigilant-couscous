#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return 0

        ldepth = self.dfs(node.left)
        rdepth = self.dfs(node.right)
        diff = abs(ldepth - rdepth)

        if ldepth == -1 or rdepth == -1 or diff > 1:
            return -1

        return 1 + max(ldepth, rdepth)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1


# @lc code=end
