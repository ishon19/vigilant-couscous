# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 0
        
        def helper(node, cur, parent):
            if not node:
                return 0

            if parent == 0 and not node.left and not node.right:
                return cur + node.val
            
            return helper(node.left, cur, 0) + helper(node.right, cur, 1)
        
        return helper(root, 0, -1)
            
