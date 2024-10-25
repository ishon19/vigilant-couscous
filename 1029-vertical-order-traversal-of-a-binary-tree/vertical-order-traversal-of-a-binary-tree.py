# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes_by_column = defaultdict(list)

        def dfs(node, col, row):
            if not node: 
                return
            
            nodes_by_column[col].append((row, node.val))

            dfs(node.left, col-1 , row+1)
            dfs(node.right, col+1, row+1)

        dfs(root, 0, 0)

        sorted_cols = sorted(nodes_by_column.keys())
        res = []

        for col in sorted_cols:
            # sort the node values too
            nodes_by_column[col].sort(key=lambda x: (x[0], x[1]))
            res.append([v for _, v in nodes_by_column[col]])

        return res
