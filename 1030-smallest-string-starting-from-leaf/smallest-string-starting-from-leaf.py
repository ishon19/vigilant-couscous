# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        
        if not root.left and not root.right:
            return chr(97 + root.val)
        
        res = 'z' * 26

        def helper(node, pattern):
            nonlocal res

            if not node:
                return
            
            if not node.left and not node.right:
                val = pattern + chr(97 + node.val)
                res = min(res, val[::-1])
            
            return helper(node.left, pattern + chr(97 + node.val)) or helper(node.right, pattern + chr(97 + node.val))
        
        helper(root, '')
        return res
        