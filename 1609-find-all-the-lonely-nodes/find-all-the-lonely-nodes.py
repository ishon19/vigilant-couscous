# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def helper(node, parent):
            if not node:
                return 
            
            if parent == 1:
                res.append(node.val)
            
            if node.left or node.right:
                if node.left and not node.right:
                    helper(node.left, 1)
                elif node.right and not node.left:
                    helper(node.right, 1)
                else:
                    helper(node.left, 0)
                    helper(node.right, 0)
        
        helper(root, -1)
        
        return res