# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:        
        if not root:
            return 0
        
        if not root.left and not root.right:
            return root.val
        
        patterns = []

        def helper(node, pattern):
            if not node:
                return 
            
            if not node.left and not node.right:
                val = pattern + str(node.val)
                # if val not in patterns:
                # print('appending', val)
                patterns.append(val)
            
            return helper(node.left, pattern + str(node.val)) or helper(node.right, pattern + str(node.val))
        
        # fill the patterns
        helper(root, '')
        
        # process the patterns
        return sum(int(pattern) if pattern != '' else 0 for pattern in patterns)
            
