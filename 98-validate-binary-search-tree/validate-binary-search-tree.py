# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=inf, high=-inf) -> bool:
        # 9th Dec 2024, 5.44 PM
        if not root:
            return True
        
        def dfs(node, left, right):
            if not node:
                return True
            
            if node.val <= left or node.val >= right:
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        
        return dfs(root, -inf, inf)
            
        # 29 Nov 2024, 8.16 PM 
        # def dfs(node, min_val, max_val):
        #     if not node:
        #         return True            
        #     if not min_val < node.val < max_val:
        #         return False            
        #     return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)        
        # return dfs(root, -inf, inf)        
        # res = []
        # def inorder(node):
        #     nonlocal res
        #     if not node:
        #         return 
        #     inorder(node.left)
        #     res.append(node.val)
        #     inorder(node.right)
        # inorder(root)
        # print('res-> ', res)
        # sort_copy = sorted(res)
        # return len(res) == len(set(res)) and res == sort_copy