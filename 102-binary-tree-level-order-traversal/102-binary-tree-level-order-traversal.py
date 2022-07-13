# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def helper(node, level):
            if not node: return 
            if level == len(ans):
                ans.append([])
            ans[level] += [node.val]
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        
        helper(root, 0)
        print(ans)
        return ans