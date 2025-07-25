# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur_num):
            if node:
                cur_num = cur_num * 10 + node.val

                if not node.left and not node.right:
                    return cur_num 
                
                left_sum = dfs(node.left, cur_num)
                right_sum = dfs(node.right, cur_num)

                return left_sum + right_sum 
            return 0
        
        return dfs(root, 0)
