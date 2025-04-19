# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forest = []
        to_delete_set = set(to_delete)
        
        def dfs(node, is_root):
            if not node:
                return None
            
            deleted = node.val in to_delete_set
            if is_root and not deleted:
                forest.append(node)
            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)
            return None if deleted else node

        dfs(root, True)
        return forest