# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        self.hm = collections.defaultdict(int)

        def dfs(node, cur):
            if node:
                cur += node.val
                if cur == targetSum:
                    self.res += 1
                self.res += self.hm[cur - targetSum]
                self.hm[cur] += 1
                dfs(node.left, cur)
                dfs(node.right, cur)

                # don't forget to remove the current sum for the sake of Recursion
                self.hm[cur] -= 1
            
        dfs(root, 0)
        return self.res