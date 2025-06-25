#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent):
            if not node:
                return 
            
            node.parent = parent
            for child in (node.left, node.right):
                dfs(child, node)
            
        dfs(root, None)
        
        res = []
        q = deque([(target, 0)])
        visited = set()

        while q:
            node, dist = q.popleft()

            if dist == k:
                res.append(node.val)
            visited.add(node)

            for child in (node.left, node.right, node.parent):
                if child and child not in visited:
                    q.append((child, dist + 1))

        return res
        
# @lc code=end