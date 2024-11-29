# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # the first entry of the preorder list is the root node
        if preorder and inorder:
            root_idx = inorder.index(preorder.pop(0))
            root_val = inorder[root_idx]
            root = TreeNode(root_val)
            root.left = self.buildTree(preorder, inorder[:root_idx])
            root.right = self.buildTree(preorder, inorder[root_idx+1:])
            return root
