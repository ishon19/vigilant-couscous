# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []

        def dfs(node, cur):
            if node:
                if not node.left and not node.right:
                    if sum(cur + [node.val]) == targetSum:
                        self.res.append(cur + [node.val])
                    return
                dfs(node.left, cur + [node.val])
                dfs(node.right, cur + [node.val])
        
        dfs(root, [])
        return self.res
