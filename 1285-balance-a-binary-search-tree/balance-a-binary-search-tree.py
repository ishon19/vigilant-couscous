# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodeValues = []
        
        def traverse(node):
            if not node:
                return 
            traverse(node.left)
            nodeValues.append(node.val)
            traverse(node.right)
        
        traverse(root)
        print(nodeValues)

        # construct balanced tree with the sorted values
        def balancedTreeFromList(arr):
            if not arr:
                return None

            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = balancedTreeFromList(arr[:mid])
            root.right = balancedTreeFromList(arr[mid+1:])

            return root
        return balancedTreeFromList(nodeValues)
        
        
        