# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def helper(start, end):
            if start > end:
                return [None]
            
            ans = []
            
            for i in range(start, end+1):
                left = helper(start, i-1)
                right = helper(i+1, end)
                
                # merge trees and add to list
                for l in left:
                    for r in right:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        ans.append(node)
            return ans
        
        return helper(1,n) if n else []