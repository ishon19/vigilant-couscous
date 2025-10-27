# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []

        def dfs(node, currSum, currPath):
            if not node:
                return 

            currSum += node.val
            currPath = currPath + [node.val]

            if not node.left and not node.right and currSum == targetSum:
                paths.append(currPath)
                return

            dfs(node.left, currSum, currPath)
            dfs(node.right, currSum, currPath)

        dfs(root, 0, [])
        return paths