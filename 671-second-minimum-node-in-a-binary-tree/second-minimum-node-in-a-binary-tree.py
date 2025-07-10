# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        traversal = []

        def dfs(node):
            if node:
                dfs(node.left)
                heappush(traversal, node.val)
                dfs(node.right)
        
        dfs(root)
        min_val = traversal[0]
        second_min = -1

        while traversal:
            second_min = heappop(traversal)
            if second_min != min_val:
                break
            else:
                second_min = -1

        return second_min
