# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = float("-inf")

        def helper(node):
            nonlocal res
            # base case
            if not node:
                return [0,0]
            else:
                l = helper(node.left)
                r = helper(node.right)

                nodesum = l[0] + r[0] + node.val
                nodecnt = l[1] + r[1] + 1
                avg = nodesum / nodecnt
                res = max(res, avg)

                return [nodesum, nodecnt]
            pass
        
        helper(root)
        return res