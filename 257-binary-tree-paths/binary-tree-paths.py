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
                print('appending', paths, res)
                if paths:
                    res.append('->'.join(paths) + '->' + str(node.val))
                else:
                    res.append(str(node.val))
                return
            if node.left:
                dfs(node.left, paths + [str(node.val)], res)
            if node.right:
                dfs(node.right, paths + [str(node.val)], res)
        res = []
        dfs(root, [], res)
        return res