# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int: 
        self.res = 0

        def helper(node, cur_min, cur_max):
            if not node:
                return
            cur_min = min(cur_min, node.val)
            cur_max = max(cur_max, node.val)
            self.res = max(self.res, cur_max - cur_min)
            helper(node.left, cur_min, cur_max)
            helper(node.right, cur_min, cur_max)
        
        helper(root, root.val, root.val)
        return self.res