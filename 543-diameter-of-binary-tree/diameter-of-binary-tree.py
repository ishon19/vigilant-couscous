# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            ldepth = dfs(node.left)
            rdepth = dfs(node.right)
            self.diameter = max(self.diameter, ldepth + rdepth)

            return 1 + max(ldepth , rdepth)
        
        self.diameter = 0
        dfs(root)
        return self.diameter
