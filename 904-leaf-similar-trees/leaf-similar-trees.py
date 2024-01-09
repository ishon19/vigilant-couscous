# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def helper(node, res):
            if not node:
                return res
            if node and not node.left and not node.right:
                res.append(node.val)
                return res
            res = helper(node.left, res)
            res = helper(node.right, res)
            return res
        
        r1 = helper(root1, [])
        r2 = helper(root2, [])
        print(r1, r2)
        return r1 == r2
