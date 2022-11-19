# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        
        def dfs(node, maxYet):
            nonlocal res
            if not node:
                return 0
            
            if maxYet <= node.val:
                res += 1            
            if node.left:
                dfs(node.left, max(node.val, maxYet))
            if node.right:
                dfs(node.right, max(node.val, maxYet))
        
        dfs(root, float("-inf"))
        return res