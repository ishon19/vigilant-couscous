# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # make the tree bidirectional
        def addParent(node, parent):
            if node:
                node.parent = parent
                addParent(node.left, node)
                addParent(node.right, node)
        
        # create the refs
        addParent(root, None)

        res = []
        seen = set()

        def dfs(node, dist):
            if node:
                if node in seen:
                    return
                seen.add(node)

                if dist == 0:
                    res.append(node.val)
                    return
                dfs(node.parent, dist - 1)
                dfs(node.left, dist - 1)
                dfs(node.right, dist - 1)
        
        dfs(target,  k)
        return res
