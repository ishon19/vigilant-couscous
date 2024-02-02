# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")

        def dfs(node):
            if not node:
                return 0
            leftmax = max(dfs(node.left), 0)
            rightmax = max(dfs(node.right), 0)
            self.res = max(self.res, leftmax + rightmax + node.val)
            return max(leftmax + node.val, rightmax + node.val)
        
        dfs(root)
        return self.res