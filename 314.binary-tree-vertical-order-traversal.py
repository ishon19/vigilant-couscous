#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        offsetMap = defaultdict(list)

        if not root:
            return []
        
        q = deque([(root, 0)])
        max_offset = min_offset = 0
        
        while q:
            node, offset = q.popleft()
            if node:
                offsetMap[offset].append(node.val)           

            min_offset = min(min_offset, offset)
            max_offset = max(max_offset, offset)

            if node.left:
                q.append((node.left, offset - 1))
            if node.right:
                q.append((node.right, offset + 1))

        return [offsetMap[offset] for offset in range(min_offset, max_offset + 1)]
        
# @lc code=end

