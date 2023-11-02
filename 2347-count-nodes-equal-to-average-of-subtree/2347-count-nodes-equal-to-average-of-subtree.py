# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal res
            # base cases
            if not node:
                return [0,0]
            else:
                l = helper(node.left)
                r = helper(node.right)

                nodesum = l[0] + r[0] + node.val
                nodeCount = l[1] + r[1] + 1

                if node.val == nodesum//nodeCount:
                    res += 1
                
                return [nodesum, nodeCount]
                
        res = 0
        helper(root)
        return res