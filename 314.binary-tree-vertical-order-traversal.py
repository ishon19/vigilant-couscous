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
        leftOffset = rightOffset = 0

        while q:
            node, offset = q.popleft()

            leftOffset = min(offset, leftOffset)
            rightOffset = max(offset, rightOffset)

            if node:
                offsetMap[offset].append(node.val)

                if node.left:
                    q.append((node.left, offset - 1))
                if node.right:
                    q.append((node.right, offset + 1))

        return [val for _, val in sorted(offsetMap.items(), key=lambda x: x[0])]

        
# @lc code=end

