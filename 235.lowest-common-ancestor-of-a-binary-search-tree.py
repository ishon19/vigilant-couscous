#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root or p == root or q == root:
            return root

        left_branch = self.lowestCommonAncestor(root.left, p, q)
        right_branch = self.lowestCommonAncestor(root.right, p, q)
        
        if left_branch and right_branch:
            return root 
        
        return left_branch if left_branch else right_branch
# @lc code=end
