# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(node):
            nonlocal res
            if not node: return 0
            l = helper(node.left)
            r = helper(node.right)
            childsum = l + r 
            if childsum == node.val: res += 1
            return childsum + node.val
        helper(root)
        return res