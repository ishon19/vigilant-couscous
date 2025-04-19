# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.diff = inf
        self.res = []

        def dfs(node):
            if not node:
                return 
            
            if abs(node.val - target) <= self.diff:
                self.diff = abs(node.val - target)
                self.res.append((self.diff, node.val))
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        self.res.sort(key=lambda x: (x[0], x[1]))
        return self.res[0][1]