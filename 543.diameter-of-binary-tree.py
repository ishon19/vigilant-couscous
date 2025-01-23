#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.diameter = 0
    
    def dfs(self, node):
        if not node:
            return 0
        
        ldepth = self.dfs(node.left)
        rdepth = self.dfs(node.right)
        self.diameter = max(self.diameter, ldepth + rdepth)
        
        return 1 + max(ldepth, rdepth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode], total=0) -> int:
        # the diameter of a binary tree is the longest path from one node 
        # to the other and so from one node, we look to the left and look to the right
        # the largest sum of the left and right depths are the answer
        self.dfs(root)
        return self.diameter

# @lc code=end

