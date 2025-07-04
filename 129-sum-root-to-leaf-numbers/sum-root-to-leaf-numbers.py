# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cumulative_sum):
            if not node:
                return 0
            
            cumulative_sum = cumulative_sum * 10 + node.val
            
            if not node.left and not node.right:
                return cumulative_sum 
            
            return dfs(node.left, cumulative_sum) + dfs(node.right, cumulative_sum)
        
        return dfs(root, 0)
                