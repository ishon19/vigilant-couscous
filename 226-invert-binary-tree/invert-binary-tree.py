# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 29 Nov 2024, 3.27 AM Attempt
        if not root:
            return None
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))
        # 28 Nov 2024, 9.01 PM Attempt
        # if not root:
        #     return None
        # return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))
        # if not root:
        #     return None
        # root.right, root.left = root.left, root.right
        # self.invertTree(root.left) 
        # self.invertTree(root.right)
        # return root