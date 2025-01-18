# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            dl = dfs(node.left)
            dr = dfs(node.right)

            if dl == -1 or dr == -1 or abs(dl-dr) > 1:
                return -1
            
            return 1 + max(dl, dr)
        
        return dfs(root) != -1