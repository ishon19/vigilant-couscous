# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, paths, res):
            if node and not node.left and not node.right:
                if paths:
                    res.append('->'.join(paths) + '->' + str(node.val))
                else:
                    res.append(str(node.val))
                return
            if node.left:
                paths.append(str(node.val))
                dfs(node.left, paths, res)
                paths.pop()
            if node.right:
                paths.append(str(node.val))
                dfs(node.right, paths, res)
                paths.pop()
        res = []
        dfs(root, [], res)
        return res