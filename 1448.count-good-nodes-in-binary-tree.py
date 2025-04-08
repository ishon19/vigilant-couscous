#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, biggestSoFar):
            if not node:
                return 

            if node.val >= biggestSoFar:
                self.count += 1
                biggestSoFar = node.val
            
            dfs(node.left, biggestSoFar)
            dfs(node.right, biggestSoFar)
        
        dfs(root, root.val)
        return self.count
# @lc code=end

