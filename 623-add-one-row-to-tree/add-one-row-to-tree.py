# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]: 
        if depth == 1:
            temp = root
            root = TreeNode(val, temp, None)
            return root       
        
        def helper(node, dep):
            if not node:
                return
            
            if dep == depth - 1:
                left = node.left
                right = node.right
                node.left = TreeNode(val, left, None)
                node.right = TreeNode(val, None, right)
                # print('added node', node.left.val, node.right.val)
        
            helper(node.left, dep + 1)
            helper(node.right, dep + 1)
        
        helper(root, 1)
        return root


            
