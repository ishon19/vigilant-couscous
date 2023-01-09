# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # preorder - left right root
        res = []

        def helper(node):
            if not node:
                return   
            res.append(node.val)         
            helper(node.left)
            helper(node.right)            
        
        helper(root)
        return res