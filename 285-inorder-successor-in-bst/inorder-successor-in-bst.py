# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        res = []

        def get_inorder(node):
            if not node:
                return 

            get_inorder(node.left)
            res.append(node)
            get_inorder(node.right)
        
        get_inorder(root)
        
        for node in res:
            if node.val > p.val:
                return node
        
        return None