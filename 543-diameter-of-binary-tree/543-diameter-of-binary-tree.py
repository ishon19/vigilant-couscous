# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def helper(node):
            if not node:
                return 0
            
            nonlocal diameter
            left_path = helper(node.left)
            right_path = helper(node.right)            
            diameter =  max(diameter, left_path + right_path)
            
            return max(right_path, left_path) + 1
        
        helper(root)
        return diameter