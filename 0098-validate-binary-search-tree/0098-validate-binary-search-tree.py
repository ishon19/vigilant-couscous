# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        
        def inorder(node):
            nonlocal res
            if not node:
                return 
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        print('res-> ', res)
        sort_copy = sorted(res)
        return len(res) == len(set(res)) and res == sort_copy