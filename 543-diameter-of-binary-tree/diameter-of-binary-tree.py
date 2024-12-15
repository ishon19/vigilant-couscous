# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.res = 0

        def helper(node):
            if not node:
                return 0
            leftDepth = helper(node.left)
            rightDepth = helper(node.right)
            self.res = max(self.res, leftDepth + rightDepth)
            return 1 + max(leftDepth, rightDepth)
        
        helper(root)
        return self.res