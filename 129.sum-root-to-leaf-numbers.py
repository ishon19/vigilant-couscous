#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur):
            if not node:
                return 0

            cur = cur * 10 + node.val 

            if not node.left and not node.right:
                return cur

            return dfs(node.left, cur) + dfs(node.right, cur)

        return dfs(root, 0)
# @lc code=end

