# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node, pattern):
            if not node:
                return 
                
            if not node.left and not node.right:
                pattern += str(node.val)
                self.res += int(pattern)
                return 
            dfs(node.left, pattern + str(node.val))
            dfs(node.right, pattern + str(node.val))
        
        dfs(root, '')
        return self.res
