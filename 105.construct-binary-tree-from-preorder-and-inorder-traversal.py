#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_q = deque(preorder)
        inorder_map = {val:idx for idx, val in enumerate(inorder)}

        def dfs(left, right):
            if left > right or not preorder_q:
                return None

            root_val = preorder_q.popleft()
            root = TreeNode(root_val)
            pivot = inorder_map[root_val]

            root.left = dfs(left, pivot - 1)
            root.right = dfs(pivot + 1, right)

            return root

        return dfs(0, len(preorder) -1)


# @lc code=end

