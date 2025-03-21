# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node, maxSoFar):
            if node:
                if node.val >= maxSoFar:
                    self.res += 1
                    maxSoFar = node.val
                dfs(node.left, maxSoFar)
                dfs(node.right, maxSoFar)
                return self.res
        
        return dfs(root, -inf)