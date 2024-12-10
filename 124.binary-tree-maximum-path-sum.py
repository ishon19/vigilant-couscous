#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # idaa is to calculate the max possible sum each node can possibly have
        # so any path crossing those nodes relay that sum to the parent
        # we can use a pre order traversal based approach 
        self.res = float("-inf")

        def dfs(node):
            if not node:
                return 0
            
            left_tree_max = max(0, dfs(node.left))
            right_tree_max = max(0, dfs(node.right))
            self.res = max(self.res, node.val + left_tree_max + right_tree_max)
            
            return node.val + max(left_tree_max, right_tree_max)
        
        dfs(root)
        return self.res
            
# @lc code=end

